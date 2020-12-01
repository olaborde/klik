
function editProfile() {
var mainFrameOne = document.getElementById("profile_view"); 
   var mainFrameTwo = document.getElementById("profile_edit");

   mainFrameOne.style.display = (
       mainFrameOne.style.display == "none" ? "block" : "none"); 
   mainFrameTwo.style.display = (
       mainFrameTwo.style.display == "none" ? "block" : "none"); 
}