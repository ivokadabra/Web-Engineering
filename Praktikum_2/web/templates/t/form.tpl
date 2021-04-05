
 <%inherit file="w.tpl"/>
  <link rel="stylesheet" href="styles.css">
     <link rel="stylesheet" href="webteams.css">

   <form id="idWTForm" action="/save" method="POST">
      <input type="hidden" value="${key_s}" id="id_spa" name="id_spa" />
      <div>
         <label for="name1_spa">1. Name</label>
         <input type="text" value="${data_o[0]}" id="name1_spa" name="name1_spa" required />
      </div>
      <div>
         <label for="vorname1_spa">1. Vorname</label>
         <input type="text" value="${data_o[1]}" id="vorname1_spa" name="vorname1_spa" required />
      </div>
      <div>
         <label for="matrnr1_spa">1. Akademische Grade</label>
         <input type="text" value="${data_o[2]}" id="akad_spa" name="akad_spa" required />
      </div>

      <div>
         <label for="semester1_spa">1. Tätigkeit</label>
         <input type="text" value="${data_o[3]}" id=tat_spa" name="tat_spa" required />
      </div>

      <div>
         <input type="submit" value="Speichern" />
         <a href="/index_2">Züruck</a>
      </div>
   </form>
