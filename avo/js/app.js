
// Lire le fichier JSON et récupérer la valeur
fetch('js/int.json')
    .then(response => response.json())
    .then(data => {
        // Stocker la valeur dans une variable
        let monEntier = data.nb_de_fichiers;
        console.log(monEntier); // Affiche 42 dans la console
        // Tu peux maintenant utiliser `monEntier` comme tu veux
    })
    .catch(error => console.error('Erreur lors de la lecture du fichier JSON:', error));




const galleryPhoto = document.querySelector("#nanogallery");



for (i = 1; i < 202; i++) {
    let myPhotos = `<a href="medias/avo${i}.jpg" data-ngThumb="medias/avo${i}.jpg"></a>`;
    galleryPhoto.innerHTML += myPhotos;
};


galleryPhoto.innerHTML += '<a href="media/avo0.mp4" data-ngThumb="img/poster.png"></a>'
// galleryPhoto.innerHTML += '<video src="/medias/avo0.mp4" controls poster></video>'

