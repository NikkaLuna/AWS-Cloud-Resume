

const counter = document.querySelector('#counter'); 

async function updateCounter() { 
    try {
        let response = await fetch("https://3rux2yezeds2brnydbv5x7mlba0zzlpj.lambda-url.us-east-2.on.aws/");
        let data = await response.json();
        counter.innerHTML = `Views: ${data.views}`; 
    } catch (error) {
        console.error("Error:", error);
    }
}

updateCounter(); 
