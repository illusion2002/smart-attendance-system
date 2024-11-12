const choice_best_friend = "Aritificial Intelligence"
const submit = document.getElementsByClassName('submi')[0];
const forgot_password
    = () => {
        let new_password_element = document.getElementsByClassName('new_pass')[0];
        let reset_pass = document.getElementsByClassName('reset_pass')[0];
        let password_box = document.getElementsByClassName('resetPassword')[0];
        let best_friend_element = document.getElementById("choice");
        let option_best_friend = best_friend_element.options[best_friend_element.selectedIndex].value.trim();
        console.log(option_best_friend);
        if (option_best_friend === choice_best_friend) {
            password_box.style.display = 'flex';
            let choice_box = document.getElementsByClassName("f_child_box")[0]
            choice_box.style.display = 'none';
            reset_pass.addEventListener("click", function () {
                let new_password = new_password_element.value.trim();
                password = new_password;
                console.log(password);
                location.href = "../html/main.html"
            })
        }

        else {
            password_box.style.display = 'none';
            alert("Incorrect Choice");
        }
    }

submit.addEventListener("click", forgot_password);