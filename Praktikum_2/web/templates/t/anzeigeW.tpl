 <%inherit file="w.tpl"/>
     
   <table>

   <tr class="customTable">
         
        
         <th>Qualifikation(1)</th>
         
      </tr>

      <tr class="customTable">
         
         <th>Bezeichnung Qualifikation(1)</th>
         <th>Beschreibung Qualifikation(1)</th>
        

         
      </tr>
     % for gosho in range(pesho):
      <tr class="customTable">
         <td>${data[gosho][0]}</td>
         <td>${data[gosho][1]}</td>
        
        
        
      </tr>
     % endfor

       <tr class="customTable">
         
         <th>Bezeichnung Zertifikat(1)</th>
         <th>Beschreibung Zertifikat(1)</th>

         
      </tr>

      <tr class="customTable">
         <td>${data_o[6]}</td>
         <td>${data_o[7]}</td>
        
        
      </tr>
    
  
   </table>
    <div>
      <a href="/index_3">zurück</a>
   </div>
   <div>
    <a href="/add_qual/data/${key_s}">Qualifikation hinzufügen</a>
    </div>
   </div>
