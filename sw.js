const CACHE_NAME = 'ephod-cache-v7.0';
const urlsToCache = [
  './',
  './index.html',
  './about.html',
  './services.html',
  './portfolio.html',
  './ongoing.html',
  './careers.html',
  './contact.html',
  './news.html',
  './privacy.html',
  './css/style.css',
  './js/main.js',
  './js/lang.js'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  const request = event.request;
  
  // Stratégie Network First pour les requêtes HTML (navigation)
  if (request.mode === 'navigate' || request.headers.get('accept').includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then(response => {
          // Met en cache la nouvelle version
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, responseClone));
          return response;
        })
        .catch(() => {
          return caches.match(request);
        })
    );
    return;
  }

  // Cache First pour le reste (images, css, js)
  event.respondWith(
    caches.match(request)
      .then(response => {
        return response || fetch(request).then(fetchRes => {
            return caches.open(CACHE_NAME).then(cache => {
                cache.put(request, fetchRes.clone());
                return fetchRes;
            });
        });
      })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(clients.claim()); // Take control of all clients immediately
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
