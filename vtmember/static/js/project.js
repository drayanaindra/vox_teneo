//Enable register button after user checks 'I have read Terms & Conditions'
$("#btn_register").live('click', function() {
 if ($(this).hasClass('disabled')){
   return false;
 }
})
$("#read_term").live('change', function() {
 if ($(this).prop('checked')) {
   $("#btn_register").removeClass('disabled');
 } else{
   $("#btn_register").addClass('disabled');
 };
})
// 

//Enable register button after user checks 'I have read Terms & Conditions'
$("#btn_pilih").live('click', function() {
 if ($(this).hasClass('disabled')){
   return false;
 }
})
$("#team{{item_1.team_1.id}}").live('change', function() {
 if ($(this).prop('checked')) {
   $("#btn_pilih").removeClass('disabled');
 } else{
   $("#btn_pilih").addClass('disabled');
 };
})

$("#team{{item_1.team_2.id}}").live('change', function() {
 if ($(this).prop('checked')) {
   $("#btn_pilih").removeClass('disabled');
 } else{
   $("#btn_pilih").addClass('disabled');
 };
})
//