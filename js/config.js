// Configuración de Firebase de tu proyecto: pagos-extreme
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyCfdMxnDiNliSsM_zmMJWfg7xAPCpw8xNg",
  authDomain: "pagos-extreme.firebaseapp.com",
  projectId: "pagos-extreme",
  storageBucket: "pagos-extreme.firebasestorage.app",
  messagingSenderId: "387072517216",
  appId: "1:387072517216:web:f1111ff501a7c9e7c10f05"
};

export const app = initializeApp(firebaseConfig);
export const db = getDatabase(app);