let email = "AI@gmail.com";
let passwor = "AIT";


const login = () => {
    let email_id = document.querySelector('input[type="email"]').value;
    let password_id = document.querySelector('input[type="password"]').value;



    //check if entered values are correct or not


    if (email_id === email && password_id === passwor) {
        window.location.href = "next.html"
    }

    else {
        alert("Invalid email and password, please try again")
    }




    console.log(email, passwor)
}

