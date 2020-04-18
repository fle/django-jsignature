(function($) {
  $(document).ready(function() {
    $(".jsign-container").each(function(){
      var config = $(this).data('config');
      var value = $(this).data('initial-value');
      $(this).jSignature(config);
      $(this).jSignature("setData", value, "native");
    });

    /* Each time user is done drawing a stroke, update value of hidden input */
    $(".jsign-container").on("change", function(e) {
      var jSignature_data = $(this).jSignature('getData', 'native');
      var django_field_name = $(this).attr('id').split(/_(.+)/)[1];
      $('#id_' + django_field_name).val(JSON.stringify(jSignature_data));
    });

    /* Bind clear button */
    $(".jsign-wrapper input").on("click", function(e) {
      $(this).siblings('.jsign-container').jSignature('reset');
    });
  });
})(jQuery || django.jQuery)
