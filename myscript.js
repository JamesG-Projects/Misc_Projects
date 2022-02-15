function handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.target);
    const uName = data.get('userName');
    sessionStorage.setItem('userName', uName);
    
    const pWord = data.get('password');
    sessionStorage.setItem("password", pWord);

    const fName = data.get('firstName');
    sessionStorage.setItem("firstName", fName);
    
    const lName = data.get('lastName');
    sessionStorage.setItem("lastName", lName);
    
    const email = data.get('email');
    sessionStorage.setItem("email", email);

    setTimeout(function() {
        location.href = "nextPage.html"
    }, 500)
}
const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);