let psw = document.getElementById('psw');

let showpsw = document.querySelector('.psword .img1 ');
let hidepsw = document.querySelector('.psword .img2 ');



const password = () => {
    console.log("this is ")

    psw.type = psw.type === 'password' ? 'text' : 'password';
    showpsw.style.display = psw.type === 'password' ? 'inline' : 'none'
    hidepsw.style.display = psw.type === 'password' ? 'none' : 'inline'

}


showpsw.addEventListener("click", password);
hidepsw.addEventListener("click", password);