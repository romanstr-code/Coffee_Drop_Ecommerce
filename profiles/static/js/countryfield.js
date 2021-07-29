// Country field 
let countrySelected = $('#id_default_country').val(); 
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4'); // If country selected get css color
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4'); // If country selected get css color
    } else {       // else you get
        $(this).css('color', '#000'); // Black color
    }
});