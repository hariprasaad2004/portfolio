let menuIcon=document.querySelector('#menu-icon');
let navbar=document.querySelector('.navbar');

menuIcon.onclick =()=>{
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

let sections=document.querySelectorAll('section');
let navlinks=document.querySelectorAll('header nav a');

window.onscroll=()=>{
    sections.forEach(sec =>{
        let top=window.scrollY;
        let offset=sec.offsetTop-150;
        let height=sec.offsetHeight;
        let id=sec.getAttribute('id');

        if(top >= offset && top < offset + height){
            navlinks.forEach(links=>{
                links.classList.remove('active');
                    document.querySelector ('header nav a[href*='+ id +']').classList.add('active');

            })
        }
    })
    let header=document.querySelector('header');
    header.classList.toggle('sticky',window.scrollY>100);

    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');
}

ScrollReveal({ 
    /*reset: true,*/
    distance:'80px',
    duration:2000,
    delay:200 
});

ScrollReveal().reveal('.home-content, .heading', { origin:'top' });
ScrollReveal().reveal('.home-img, .service-container, .portfolio-box, .contact form', { origin:'bottom' });
ScrollReveal().reveal('.home-content h1, .about-img', { origin:'left' });
ScrollReveal().reveal('.home-content p, .about-content', { origin:'right' });

const typed=new Typed('.multiple-text',{
    strings:['Full-Stack Developer','Web Developer'],
    typeSpeed:100,
    backSpeed:100,
    backDelay:1000,
    loop:true
})
function sendMessage(event) {
    event.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: 
            "Mobile: " + document.getElementById("mobile").value + "\n" +
            "Subject: " + document.getElementById("subject").value + "\n\n" +
            document.getElementById("message").value
    };

    fetch("http://127.0.0.1:5000/sendmail", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        alert("Message Sent Successfully!");
        document.getElementById("contactForm").reset();
    })
    .catch(err => {
        alert("Error sending message!");
        console.log(err);
    });
}