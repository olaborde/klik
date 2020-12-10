
function editProfile() {
    var mainFrameOne = document.getElementById("profile_view"); 
    var mainFrameTwo = document.getElementById("profile_edit");

   mainFrameOne.style.display = (
       mainFrameOne.style.display == "none" ? "block" : "none"); 
   mainFrameTwo.style.display = (
       mainFrameTwo.style.display == "none" ? "block" : "none"); 
}

function editComment() {
    var mainFrameOne = document.getElementById("profile"); 
    var mainFrameTwo = document.getElementById("comment_edit");

   mainFrameOne.style.display = (
       mainFrameOne.style.display == "none" ? "block" : "none"); 
   mainFrameTwo.style.display = (
       mainFrameTwo.style.display == "none" ? "block" : "none");  
}
function activaTab(tab){
    $('.nav-tabs a[href="#' + tab + '"]').tab('show');
};