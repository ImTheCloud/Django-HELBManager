function afficherPopup() {
  alert(`Task or subtask moved:`);
}


const list_items = document.querySelectorAll('.list-item');
const lists = document.querySelectorAll('.list');

let draggedItem = null;


function saveDraggedItemLocation(e) {
  console.log('saveDraggedItemLocation called');

  // Empêcher le comportement par défaut de l'événement drop
  e.preventDefault();
  // Récupérer l'élément de liste cible de l'événement drop
  const targetList = e.target;
  // Vérifier que l'élément glissé-déposé est défini
  if (draggedItem && targetList.matches('.list')) {

 
    console.log(`Dragged item: ${draggedItem.id}`);
    // Enregistrer l'emplacement de l'élément glissé-déposé dans le stockage local
    localStorage.setItem(draggedItem.id, targetList.id);

    // Ajouter l'élément glissé-déposé à l'élément de liste cible
    targetList.append(draggedItem);
  
  let elementAdded = true;
  localStorage.setItem('elementAdded', elementAdded);

    
  }
  
}











function restoreDraggedItemLocations() {
  console.log('restoreDraggedItemLocations function called');
  // Récupérer tous les éléments de liste
  const list_items = document.querySelectorAll('.list-item');

  // Pour chaque élément de liste, récupérer son emplacement enregistré dans le stockage local
  for (const list_item of list_items) {
    const location = localStorage.getItem(list_item.id);
	console.log(`location for ${list_item.id}: ${location}`);
    // Si un emplacement a été enregistré pour cet élément, ajouter l'élément à l'élément de liste correspondant
    if (location) {
      // Récupérer l'élément de liste cible
      const targetList = document.getElementById(location);
      // Vérifier que l'élément cible est bien une liste (et non un élément de liste-item)
      if (targetList.classList.contains('list')) {
        console.log(`adding ${list_item.id} to ${location}`);

        targetList.append(list_item);
      }
    }
  }
}

for (let i = 0; i < list_items.length; i++) {
  const item = list_items[i];

  item.addEventListener('dragstart', function () {
    draggedItem = item;
    setTimeout(function () {
      item.style.display = 'none';
    }, 0);
  });

  item.addEventListener('dragend', function () {
    setTimeout(function () {
      draggedItem.style.display = 'block';
      draggedItem = null;
    }, 0);
  });

  }

for (let j = 0; j < lists.length; j++) {
  const list = lists[j];

  list.addEventListener('dragover', function (e) {
    e.preventDefault();
  });

  list.addEventListener('dragenter', function (e) {
    e.preventDefault();
    this.style.backgroundColor = 'rgba(0, 0, 0, 0.2)';
  });

  list.addEventListener('dragleave', function (e) {
    this.style.backgroundColor = 'rgba(0, 0, 0, 0.1)';
  });

  list.addEventListener('drop', saveDraggedItemLocation);

}

// Lorsque la page est chargée, restaurer l'emplacement de chaque élément glissé-déposé
window.addEventListener('load', restoreDraggedItemLocations);