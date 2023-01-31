const user = document.querySelector(".fa-user ");
const menu = document.querySelector(".fa-bars ");
const loginlogout = document.querySelector(".login-logout");

user.addEventListener("click", () => {

 
  loginlogout.classList.toggle("active");

});


menu.addEventListener("click", () => {
  menu.classList.toggle("fa-circle-xmark");
 
});


const message = document.querySelector('.message')

window.onload = () => {
  setTimeout(() => {
    message.setAttribute("style", "display:none");
    console.log("welcome sara ");
  }, 3000);
}