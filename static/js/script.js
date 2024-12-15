function theme() {
    const theme_btn = document.querySelector(".light_mode");
    const body = document.querySelector("body");

    body.classList.toggle("light_mode_active");
    theme_btn.classList.toggle("light_mode_active");

    theme_btn.innerHTML = theme_btn.classList.contains("light_mode_active") ? "<i class='fa-solid fa-cloud-moon'></i>" : "<i class='fa-solid fa-sun-plant-wilt'></i>";
}

document.querySelector("#extractbtn").addEventListener("click", function(event) {
    event.preventDefault();

    const url = document.querySelector("#url").value;
    const choice = document.querySelector("input[name='options']:checked").value;
    const tagn = document.querySelector("#tagn").value;

    if (!url || !choice) {
        alert("Please enter a URL and select an extraction option.");
        return;
    }

    const formData = new FormData();
    formData.append('url', url);
    formData.append('choice', choice);
    formData.append('tagn', tagn);

    fetch('/scrape', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        const resultContainer = document.querySelector('.extracted-content #extractedText');
        resultContainer.textContent = data; 

        const contentContainer = document.querySelector('.extracted-content');
        contentContainer.style.display = 'block'; 
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while processing the request.");
    });
});

document.querySelector('.cpy').addEventListener('click', function() {
    const content = document.querySelector('.extracted-content #extractedText').textContent;
    const textarea = document.createElement('textarea');

    textarea.value = content;
    document.body.appendChild(textarea);

    textarea.select();
    document.execCommand('copy');

    document.body.removeChild(textarea);

    const copyButton = document.querySelector('.cpy');
    copyButton.innerHTML = 'Copied! <i class="fa-solid fa-check"></i>';

    setTimeout(() => {
        copyButton.innerHTML = 'copy <i class="fa-solid fa-copy"></i>';
    }, 2000);
});
