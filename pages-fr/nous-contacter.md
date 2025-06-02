---
published: true
permalink: /nous-contacter/
category: Divers
title: Nous contacter
gallery:
  - /assets/uploads/pxl_20240513_090804955-sd.jpg
order: "30"
---
### Centre d’Initiation à la Nature d’Auberive (CIN)

**Maison de Pays d’Auberive (octobre à mars)**
1 rue fermiers

**Maison forestière de Charbonnières (avril à septembre)**
9 chemin du val Clavin

Boite postale n°9<br>
52160 Auberive

03 25 84 71 86 – 06 98 91 71 86

cin.auberive@ligue52.org 

Q3H4+3Q Auberive


<form name="contact" netlify>
  <p>
    <label>Name <input type="text" name="name" /></label>
  </p>
  <p>
    <label>Email <input type="email" name="email" /></label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
</form>
<script>
const handleSubmit = event => {
  event.preventDefault();

  const myForm = event.target;
  const formData = new FormData(myForm);

  fetch("/", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams(formData).toString()
  })
    .then(() => alert("Merci pour votre message et à très bientôt"))
    .catch(error => alert(error));
};

document.querySelector("contact").addEventListener("submit", handleSubmit);
</script>