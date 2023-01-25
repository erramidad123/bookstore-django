const user = document.querySelector(".fa-user ");
const menu = document.querySelector(".fa-bars ");
const loginlogout = document.querySelector(".login-logout");

user.addEventListener("click", () => {

 
  loginlogout.classList.toggle("active");

});


menu.addEventListener("click", () => {
  menu.classList.toggle("fa-circle-xmark");
 
});
