 <%inherit file="w.tpl"/>

   <form id="idWTForm" action="/save_qual" method="POST">
      <input type="hidden" value="${key_s}" id="id_w" name="id_w" />
      <div>
         <label for="name1_spa">Beschreibung</label>
         <input type="text" value="${data_o[0]}" id="beschreibung_qual" name="beschreibung_qual" required />
      </div>
      <div>
         <label for="vorname1_spa">Bezeichnung</label>
         <input type="text" value="${data_o[1]}" id="bis_qual" name="bis_qual" required />
      </div>
      
      <div>
         <input type="submit" value="Speichern" />
         <a href="/index">Züruck</a>
      </div>
   </form>
