if('serviceWorker' in navigator){
    navigator.serviceWorker.register('../sw.js')
    .then(reg => console.log('service worker registered'))
    .catch(()=>console.log('service worker not registered'))
  }