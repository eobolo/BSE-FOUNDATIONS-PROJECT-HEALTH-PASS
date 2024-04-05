// THIS IS FOR THE LOADING PAGE

window.addEventListener('load', function() {

    const logo = document.getElementById('loading-logo');


    // Fading in of the logo
    setTimeout(() => {
        logo.style.opacity = 1; // the logo is now fully faded in
    }, 500); 



    // Starting fadding # out
    setTimeout(() => {

        const loadingScreen = document.getElementById('loading');
        loadingScreen.style.opacity = 0; 
        loadingScreen.style.transition = 'opacity 2.5s ease-in-out';
    }, 3000);



    // Removoving the loading page
    setTimeout(() => {
        const loadingScreen = document.getElementById('loading');
        loadingScreen.style.display = 'none';


        // Opening the sign up or sign in page
        window.location.href = 'login.html';

    }, 5600);
});


