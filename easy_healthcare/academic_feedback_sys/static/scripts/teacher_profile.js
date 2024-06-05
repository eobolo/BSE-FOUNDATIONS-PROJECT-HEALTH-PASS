const initializeDB = () => {
    const request = indexedDB.open('imageDB', 1);

    request.onupgradeneeded = function (event) {
        const db = event.target.result;
        if (!db.objectStoreNames.contains('images')) {
            db.createObjectStore('images', { keyPath: 'id' });
        }
    };

    request.onsuccess = function () {
        console.log('Database initialized successfully');
    };

    request.onerror = function (event) {
        console.error('Database initialization error:', event.target.errorCode);
    };
};

const handleImageUpload = (event, userId) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imageData = e.target.result;
            saveImageToDB(imageData, userId);
        };
        reader.readAsDataURL(file);
    }
}

const saveImageToDB = (imageData, userId) => {
    const request = indexedDB.open('imageDB', 1);
    request.onsuccess = function (event) {
        const db = event.target.result;
        const transaction = db.transaction(['images'], 'readwrite');
        const store = transaction.objectStore('images');
        store.put({ id: `${userId}`, data: imageData });
    };
}
const loadImageFromDb = (userId, imgElement) => {
    //make a request to the database based string and int
    // we used to save it.
    const request = indexedDB.open('imageDB', 1);
    request.onsuccess = function (event) {
        const db = event.target.result;
        const transaction = db.transaction(['images'], 'readonly');
        const store = transaction.objectStore('images');
        const getRequest = store.get(`${userId}`);
        getRequest.onsuccess = function (event) {
            const result = event.target.result;
            if (result) {
                console.log("loading data successfully");
                imgElement.src = result.data;
            } else {
                imgElement.src = "";
            }
        };
    };

    request.onerror = function () {
        imgElement.src = "";
    }
}

const uploadImageInput = document.querySelector(".upload-image");
uploadImageInput.addEventListener("change", (event) => {
    const userId = event.target.id;
    const receiveImageInput = document.querySelector(".profile__image");
    initializeDB();
    handleImageUpload(event, userId);
    loadImageFromDb(userId, receiveImageInput);
    location.reload();
});

document.addEventListener("DOMContentLoaded", () => {
    const uploadImageInput = document.querySelector(".upload-image");
    const receiveImageInput = document.querySelector(".profile__image");
    const userId = uploadImageInput.id;
    initializeDB();
    loadImageFromDb(userId, receiveImageInput);
})