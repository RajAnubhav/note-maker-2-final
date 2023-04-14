const staticCacheName = 'site-static-v1';
const dynamicCache = 'site-dynamic-v1';
const assets = [
  '/',
  './templates/mysite/index.html',
  './templates/mysite/add_post.html',
  './templates/mysite/article_details.html',
  './templates/mysite/base.htlm',
  './templates/mysite/category_post.html',
  './templates/mysite/code_editor.html',
  './templates/mysite/dashboard.html',
  './templates/mysite/delete_post.html',
  './templates/mysite/edit_post.html',
  './templates/mysite/page1.html',
  './templates/categories.html',
  './logo.png',
  './members/templates/registration/change_password.html',
  './members/templates/registration/edit_profile.html',
  './members/templates/registration/login.html',
  './members/templates/registration/registration.html',
  './app.js',
];

// cache size limit function
const limitCacheSize = (name, size)=>{
  caches.open(name).then(cache=>{
    cache.keys().then(keys=>{
      if(keys.length>size){
        cache.delete(keys[0]).then(limitCacheSize(name, size));
      }
    })
  })
}

// install event fires when the service worker is changed
self.addEventListener('install', evt => {
  // console.log('service worker installed');
  evt.waitUntil(
    caches.open(staticCacheName).then(cache=>{
      console.log('caching shell assets');
      cache.addAll(assets)
    })
  );
});

// activate event
self.addEventListener('activate', evt => {
  // console.log('service worker activated');
  // delete all the old caches
  evt.waitUntil(
    caches.keys().then(keys=>{
      console.log(keys); //
      return Promise.all(keys
        .filter(key=>key !== staticCacheName))
        .map(key=>caches.delete())
    })
  );

});

