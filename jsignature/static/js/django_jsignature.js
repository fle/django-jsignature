$(document).ready(function() {

  /* Each time user is done drawing a stroke, update value of hidden input */
  $(document).delegate(".jsign-container", "change", function(e) {
    var jSignature_data = $(this).jSignature('getData', 'native');
    var django_field_name = $(this).attr('id').split(/_(.+)/)[1];
    $('#id_' + django_field_name).val(JSON.stringify(jSignature_data));
  });

  /* Bind clear button */
  $(document).delegate(".jsign-wrapper input", "click", function(e) {
    $(this).siblings('.jsign-container').jSignature('reset');
  });

})
