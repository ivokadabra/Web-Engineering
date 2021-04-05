function confirmDelete_p (event_opl) {
   if ((event_opl.target.tagName.toLowerCase() == 'a'       ) &&
       (event_opl.target.className             == "clDelete")    ) {
      if(confirm('Wolle sie den Dateneinsatz wirklich löschen!')){

      }else{ event_opl.preventDefault()}
   }
}
window.onload = function () {
   let body_o = document.getElementsByTagName('body')[0];
   body_o.addEventListener('click', confirmDelete_p, false);
}