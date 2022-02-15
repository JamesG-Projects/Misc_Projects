function handleSubmit(event) {
   event.preventDefault();
   const data = new FormData(event.target);

   if(data.get('userName') == sessionStorage.getItem('userName'))
   {
      if(data.get('password') == sessionStorage.getItem('password'))
      {
        let fName = sessionStorage.getItem('firstName').toString();
        document.getElementById("fName").innerHTML = fName;
        console.log(fName);

        let lName = sessionStorage.getItem('lastName').toString();
        document.getElementById("lName").innerHTML = lName;

        let email = sessionStorage.getItem('email').toString();
        document.getElementById("email").innerHTML = email;
      }
   }
}
const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);