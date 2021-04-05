
    <%inherit file="w.tpl"/>
     
   <table>


      <tr class="customTable">
         <th>teilnehmen</th>
    </tr>

      <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
         <th>Status(1)</th>
         <th>Zertifikate(1)</th>
         
      </tr>
      % for p in range(i):
      <tr class="customTable">
         <td>${data_u[p][0]}</td>
         <td>${data_u[p][1]}</td>
         <td>${data_u[p][2]}</td>
         <td>${data_u[p][3]}</td>
         <td>${data_u[p][4]}</td>
         <td>${data_u[p][5]}</td>
         
         <td>${data_st[p]}</td>
         <td>${data_zer[p]}</td>
        
         
        
      </tr>
    
     % endfor
     <tr class="customTable">
         <th>Für dennen man sich anmelden will</th>
    </tr>

      <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
        
         
      </tr>
      % for key_s in data_o:
      <tr class="customTable">
         <td>${data_o[key_s][0]}</td>
         <td>${data_o[key_s][1]}</td>
         <td>${data_o[key_s][2]}</td>
         <td>${data_o[key_s][3]}</td>
         <td>${data_o[key_s][4]}</td>
         <td>${data_o[key_s][5]}</td>
        
         
         
         
        <td><a href="/mit_id/${key_s}/${id}">anmelden</a></td>
        
      </tr>
      % endfor
   </table>
   <div>
      <a href="/add">erfassen</a>
   </div>
    <div>
      <a href="/index_2">zurück</a>
   </div>
