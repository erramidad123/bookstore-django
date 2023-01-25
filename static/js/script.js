const user = document.querySelector(".fa-user ");
const loginlogout = document.querySelector(".login-logout");

user.addEventListener("click", () => {

  user.classList.toggle("fa-xmark");
  loginlogout.classList.toggle("active");

});
