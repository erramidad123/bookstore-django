const user = document.querySelector('.fa-user '); 
const loginlogout = document.querySelector('.login-logout') 

user.addEventListener('click',()=>{
    loginlogout.classList.toggle('active')
})