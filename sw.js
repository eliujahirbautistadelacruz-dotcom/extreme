let alumnosLocal = {};

self.addEventListener('message', (event) => {
    if (event.data.type === 'SINC_ALUMNOS') {
        alumnosLocal = event.data.alumnos;
    }
});

// Chequeo en segundo plano cada 30 segundos
setInterval(() => {
    const ahora = new Date();
    for (const id in alumnosLocal) {
        const u = alumnosLocal[id];
        const difMs = new Date(u.vencimiento) - ahora;
        const mins = Math.floor(difMs / 60000);

        if (mins >= 1 && mins <= 4) {
            self.registration.showNotification(`EXTREME: ${u.nombre}`, {
                body: `¡Atención! Quedan ${mins} minutos.`,
                tag: `bg-notif-${u.nombre}-${mins}`,
                renotify: true
            });
        }
    }
}, 30000);

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (event) => event.waitUntil(clients.claim()));