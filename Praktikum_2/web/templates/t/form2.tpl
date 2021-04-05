 <%inherit file="w.tpl"/>


   <form id="idWTForm" action="/save2" method="POST">
      <input type="hidden" value="${key_s}" id="id_spa" name="id_spa" />
      <div>
         <label for="name1_spa">Bezeichnung</label>
         <input type="text" value="${data_o[0]}" id="bezeichnung_spa" name="bezeichnung_spa" required />
      </div>
      <div>
         <label for="vorname1_spa">Von</label>
         <input type="date" value="${data_o[1]}" id="von_spa" name="von_spa" required />
      </div>
      <div>
         <label for="matrnr1_spa">Bis</label>
         <input type="date" value="${data_o[2]}" id="bis_spa" name="bis_spa" required />
      </div>

      <div>
         <label for="semester1_spa">Beschreibung</label>
         <input type="text" value="${data_o[3]}" id=beschreibung_spa" name="beschreibung_spa" required />
      </div>
      <div>
         <label for="matrnr1_spa">Maximale Teilnehmeranzahl</label>
         <input type="number" value="${data_o[4]}" id="max_spa" name="max_spa" required />
      </div>

      <div>
         <label for="semester1_spa">Minimale Teilnehmeranzahl</label>
         <input type="number" value="${data_o[5]}" id=min_spa" name="min_spa" required />
      </div>
      <div>
         <label>Eingabe für Zertifikat</label>
      
      </div>
      <div>
         
      
      </div>
      <div>
         <label for="matrnr1_spa">Bezeichnung</label>
         <input type="text" value="${data_o[6]}" id="zer_besch" name="zer_besch" required />
      </div>

      <div>
         <label for="semester1_spa">Beschreibung</label>
         <input type="text" value="${data_o[7]}" id="zer_bez" name="zer_bez" required />
      </div>

     <div>
         <input type="submit" value="Speichern" />
         <a href="/index_3">Züruck</a>
      </div>
   </form>
