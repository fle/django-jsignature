"""
    Very inspired by zivezab's django-autograph
    https://github.com/zivezab/django-autograph/blob/master/autograph/utils.py
"""
import json
from itertools import chain
from PIL import Image, ImageDraw, ImageOps, __version__ as PIL_VERSION

AA = 5  # super sampling for antialiasing


def draw_signature(data, as_file=False):
    """Draw signature based on lines stored in json_string.
    `data` can be a json object (list in fact) or a json string
    if `as_file` is True, a temp file is returned instead of Image instance
    """

    def _remove_empty_pts(pt):
        return {
            "x": list(filter(lambda n: n is not None, pt["x"])),
            "y": list(filter(lambda n: n is not None, pt["y"])),
        }

    if isinstance(data, str):
        drawing = json.loads(data, object_hook=_remove_empty_pts)
    elif isinstance(data, list):
        drawing = data
    else:
        raise ValueError

    # Compute box
    padding = 10
    min_width = int(round(min(chain(*[d["x"] for d in drawing])))) - padding
    max_width = int(round(max(chain(*[d["x"] for d in drawing])))) + padding
    width = max_width - min_width
    min_height = int(round(min(chain(*[d["y"] for d in drawing])))) - padding
    max_height = int(round(max(chain(*[d["y"] for d in drawing])))) + padding
    height = max_height - min_height

    # Draw image
    im = Image.new("RGBA", (width * AA, height * AA))
    draw = ImageDraw.Draw(im)
    for coords in drawing:
        line_length = len(coords["x"])
        if line_length == 1:
            # This is a single point, convert to a circle of 2x2 AA pixels
            draw.ellipse(
                [
                    (
                        (coords["x"][0] - min_width) * AA,
                        (coords["y"][0] - min_height) * AA,
                    ),
                    (
                        (coords["x"][0] - min_width + 2) * AA,
                        (coords["y"][0] - min_height + 2) * AA,
                    ),
                ],
                fill="#000",
            )
        else:
            points = [
                ((coords["x"][i] - min_width) * AA, (coords["y"][i] - min_height) * AA)
                for i in range(0, line_length)
            ]
            draw.line(points, fill="#000", width=2 * AA)
    im = ImageOps.expand(im)
    # Smart crop
    bbox = im.getbbox()
    if bbox:
        im.crop(bbox)

    im.thumbnail(
        (width, height),
        # Image.ANTIALIAS is replaced in PIL 10.0.0
        Image.ANTIALIAS if int(PIL_VERSION.split(".")[0]) < 10 else Image.LANCZOS,
    )

    if as_file:
        ret = im._dump(format="PNG")
    else:
        ret = im

    return ret
