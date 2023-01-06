///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//https://www.youtube.com/watch?v=tZ45HZAkbLc voici la video d'ou j'ai pu effectuer le drag & drop mais, il est modifier
// car l'enregistrement ne se faisait pas lorsque je rafraichissait la page
// Afin de réussir l'enregistrement j'ai du ajouté un stochage local a chaque rafraichissement de page.
//Drag & drop :
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

const list_items = document.querySelectorAll('.list-item');
const lists = document.querySelectorAll('.list');
const consoleDiv = document.querySelector('.notification');

// Function pour sauvegarder les elemetns dans le stockage local
function saveDraggedItemLocation(e) {
  e.preventDefault();
  const targetList = e.target;
  if (draggedItem && targetList.matches('.list')) {
    localStorage.setItem(draggedItem.id, targetList.id);
    consoleDiv.innerHTML += `The status of task ${draggedItem.id}  has been moved to ${targetList.id} by ${userName}</br>`
    targetList.append(draggedItem);
    localStorage.setItem('consoleMessage', consoleDiv.innerHTML);
  }
}
consoleDiv.innerHTML = localStorage.getItem('consoleMessage');


// Fonction pour restaurer l'emplacement de chaque élément de liste en se basant sur les données enregistrées dans le stockage local
function restoreDraggedItemLocations() {
  console.log('restoreDraggedItemLocations function called');
  const list_items = document.querySelectorAll('.list-item');
  for (const list_item of list_items) {
    const location = localStorage.getItem(list_item.id);
    console.log(`location for ${list_item.id}: ${location}`);
    // Si un emplacement a été enregistré pour cet élément, ajouter l'élément à l'élément de liste correspondant
    if (location) {
      const targetList = document.getElementById(location);
      // Vérifier que l'élément cible est bien une liste
      if (targetList.classList.contains('list')) {
        console.log(`adding ${list_item.id} to ${location}`);
        targetList.append(list_item);
      }
    }
  }
}


// Ajouter des gestionnaires d'événements du drag & drop  aux éléments de liste
for (let i = 0; i < list_items.length; i++) {
  // Récupérer l'élément de liste courant
  const item = list_items[i];
  item.addEventListener('dragstart', function () {
    // Définir l'élément de liste courant comme l'élément drag & drop 
    draggedItem = item;
    setTimeout(function () {
      item.style.display = 'none';
    }, 0);
  });

  // Gestionnaire d'événement pour la fin du drag & drop d'un élément de liste
  item.addEventListener('dragend', function () {
    // Afficher l'élément de liste à nouveau une fois le  drag & drop terminé
    setTimeout(function () {
      draggedItem.style.display = 'block';
      draggedItem = null;
    }, 0);
  });
}

// Ajouter des gestionnaires d'événements du drag & drop aux éléments de liste
for (let j = 0; j < lists.length; j++) {
  const list = lists[j];
  list.addEventListener('dragover', function (e) {
    // Empêcher le comportement par défaut de l'événement
    e.preventDefault();
  });

  list.addEventListener('dragenter', function (e) {
      e.preventDefault();

    });
  
    list.addEventListener('drop', saveDraggedItemLocation);
  }
  
  // Lorsque la page est chargée, restaurer l'emplacement de chaque élément glissé-déposé en se basant sur les données enregistrées dans le stockage local
  window.addEventListener('load', restoreDraggedItemLocations);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
// Le chat : 
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  
const userName = document.querySelector('.user-connected').textContent;
const input = document.getElementById("message");
const chatDiv = document.getElementById("chat");
const sendButton = document.getElementById("send");
const deleteButton = document.getElementById("delete-btn");
const deleteAllButton = document.getElementById("delete-all-btn");
  
// messages enregistrés dans le stockage local
let messages = loadMessages();
displayMessages();
  
sendButton.addEventListener("click", sendMessage);
deleteButton.addEventListener("click", deleteMessage);
deleteAllButton.addEventListener("click", deleteAllMessages);
  
// Affiche les messages sur la page
function displayMessages() {
    chatDiv.innerHTML = messages.join("<br>");
}
  
// Envoie un message au chat
function sendMessage() {
    let message = input.value;
    let fullMessage = `${userName} : ${message}`;
    messages.push(fullMessage);
    saveMessages(messages);
    displayMessages();
}
  // Supprime le dernier message du chat
  function deleteMessage() {
    {
      messages.pop();
      saveMessages(messages);
      displayMessages();
  }
}
    
  // Supprime tous les messages du chat
  function deleteAllMessages() {
      messages = [];
      saveMessages(messages);
      displayMessages();
  }
    
  // Messages enregistrés dans le stockage local
  function loadMessages() {
      return JSON.parse(localStorage.getItem("messages")) || [];
  }
    
  // Enregistre les messages dans le stockage local
  function saveMessages(messages) {
      localStorage.setItem("messages", JSON.stringify(messages));
  }


  