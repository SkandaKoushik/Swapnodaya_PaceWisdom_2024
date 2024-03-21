
let message = document.getElementById("status");
let image = document.getElementById("img-status")

let messageOnline = () => {
    message.textContent = "Internet Connection Available";
    message.style.cssText = "background-color: #e7f6d5; color: #689f38";

    image.src = "images/connected.jpg";
};

let messageOffline = () => {
    message.textContent = "No Internet Connection";
    message.style.cssText = "background-color: #ffdde0; color: #d32f2f";

    image.src = "images/no-connection.jpg";
};


if (window.navigator.onLine) {
    messageOnline();
} 
else {
    messageOffline();
}


window.addEventListener("online", messageOnline);
window.addEventListener("offline", messageOffline);



