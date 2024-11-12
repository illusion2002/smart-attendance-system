let email = "admin@gmail.com";
let passwor = "qwerty123";


const login = () => {
    let email_id = document.querySelector('input[type="email"]').value;
    let password_id = document.querySelector('input[type="password"]').value;



    //check if entered values are correct or not


    if (email_id === email && password_id === passwor) {
        window.location.href = "admin.html"
    }

    else {
        alert("Invalid email and password, please try again")
    }




    console.log(email, passwor)
}

