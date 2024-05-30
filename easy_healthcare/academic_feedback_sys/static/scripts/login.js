        const userUsername = document.querySelector("#id_username");
        const userPassword = document.querySelector("#id_password");

        userUsername.addEventListener("click", () => {
            const usernameIcon = document.querySelector(".user-icon");
            usernameIcon.style.color = "#000";
        })
        userUsername.addEventListener("blur", () => {
            const usernameIcon = document.querySelector(".user-icon");
            usernameIcon.style.color = "#c6c3c3";
        })

        userPassword.addEventListener("click", () => {
            const passwordIcon = document.querySelector(".password-icon");
            passwordIcon.style.color = "#000";
        })
        userPassword.addEventListener("blur", () => {
            const passwordIcon = document.querySelector(".password-icon");
            passwordIcon.style.color = "#c6c3c3";
        });
