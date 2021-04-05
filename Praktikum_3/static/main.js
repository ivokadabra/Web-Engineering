//------------------------------------------------------------------------------
//Demonstrator evs/tco/tmg
//------------------------------------------------------------------------------
// rev. 1, 18.12.2020, Bm
// rev. 0, 21.11.2018, Bm
//------------------------------------------------------------------------------
// hier zur Vereinfachung (!) die Klassen in einer Datei

'use strict'

//------------------------------------------------------------------------------

class Anmelden {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/anmelden/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
            console.log(error_opl);
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }

   send_data(id_spl) {
      let path_s = "/anmelden/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            let parsedData = JSON.parse(result_spl);
            var result = parsedData.find(obj => {
               return obj.id === String(id_spl)
            })
            requester_o.POST_px("/anmelden/?data=" + JSON.stringify(result));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
            console.log(error_opl);
         });
   }

   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "anmelden_weit") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.app_o.anmelde_View_o.send_data(elx_o.id);
            elx_o.classList.remove("clSelected");
         }
         event_opl.preventDefault();
      }
   }
}



class Qual {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/qual_in_weit/" + id_spl;

      //const fs = require('fs');

      //let data = JSON.stringify(id_spl);
      //fs.writeFileSync('data/temp.json', data);

      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            if (result_spl != []) {
               this.doRender_p(JSON.parse(result_spl), id_spl)
            } else {
               alert("keine Qualifikationen, wollen Sie neue Hinzufügen");
            };
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl, id) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);

      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }

   }

   configHandleEvent_p() {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }

   }
}





class Weiterbildung_in_Mit_View_cl {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/weit_mit/" + id_spl;

      //const fs = require('fs');

      //let data = JSON.stringify(id_spl);
      //fs.writeFileSync('data/temp.json', data);

      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            if (result_spl != []) {
               this.get_status(id_spl, JSON.parse(result_spl));
            } else {
               alert("keine Weiterbildungen ");
            };
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }

   get_status(id, data) {
      let requester_o = new APPUTIL.Requester_cl();
      let path = "/status/" + id;
      requester_o.GET_px(path)
         .then(result_spl => {
            if (result_spl != []) {
               this.doRender_p(JSON.parse(result_spl),data);
            } else {
               alert("kein Status ");
            };
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }

   doRender_p(data_opl,data_weit) {
      var list = []
     
      list.push(data_weit);
      list.push(data_opl);
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, list);
      let el_o = document.querySelector(this.el_s);

      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }

   }

   configHandleEvent_p() {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }

   }
}

class FormWeiter_cl {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;

   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/weiterbildung/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      data_opl = []
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      var proba;
      var proba_1;
      var proba_2;
      var proba_3;
      var proba_4;
      var proba_5;
      var proba_6;
      var proba_7;

      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if (event_opl.target.id == "speichern") {
         proba = document.getElementById("col1").value;
         proba_1 = document.getElementById("col2").value;
         proba_2 = document.getElementById("col3").value;
         proba_3 = document.getElementById("col4").value;
         proba_4 = document.getElementById("col5").value;
         proba_5 = document.getElementById("col6").value;
         proba_6 = document.getElementById("col7").value;
         proba_7 = document.getElementById("col8").value;
         //var Proba=proba.concat(proba_1);
         var Proba = [proba, proba_1, proba_2, proba_3, proba_4, proba_5, proba_6, proba_7];
         let requester_o = new APPUTIL.Requester_cl();
         var myJSON = JSON.stringify(Proba);
         let path_s = "/weiterbildung/?data=" + myJSON;

         requester_o.POST_px(path_s, myJSON);
         //APPUTIL.es_o.publish_px("app.cmd", ["weiterbildung", null]);
         event_opl.preventDefault();
      }




   }
}

class QualForm_cl {
   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/qual/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();

      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });

   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      var proba;
      var proba_1;
      //var proba_2;

      var id;

      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if (event_opl.target.id == "speichern") {

         proba = document.getElementById("col1").value;
         proba_1 = document.getElementById("col2").value;
        // proba_2 = document.getElementById("col3").value;

         id = document.getElementById("id").value;
         //var Proba=proba.concat(proba_1);
         var Proba = [id, proba, proba_1];
         let requester_o = new APPUTIL.Requester_cl();
         var myJSON = JSON.stringify(Proba);
         let path_s = "/qual/?data=" + myJSON;


         requester_o.POST_px(path_s, myJSON);
         APPUTIL.es_o.publish_px("app.cmd", ["weiterbildung", null]);
         event_opl.preventDefault();
      }
   }
}


class FormView_cl {
   //------------------------------------------------------------------------------
   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/mitarbeiter/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });

   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      var proba;
      var proba_1;
      var proba_2;
      var proba_3;

      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if (event_opl.target.id == "speichern_mit_new") {

         proba = document.getElementById("col1").value;
         proba_1 = document.getElementById("col2").value;
         proba_2 = document.getElementById("col3").value;
         proba_3 = document.getElementById("col4").value;

         //var Proba=proba.concat(proba_1);
         var Proba = [proba, proba_1, proba_2, proba_3];
         let requester_o = new APPUTIL.Requester_cl();
         var myJSON = JSON.stringify(Proba);
         let path_s = "/mitarbeiter/?data=" + myJSON;


         requester_o.POST_px(path_s, myJSON);
        // APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }
   }
}

class Delete_weit_cl {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/weiterbildung/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      var Proba = requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl), id_spl);
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });




   }
   doRender_p(data_opl, id) {
      //let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let requester_o = new APPUTIL.Requester_cl();

      requester_o.DELETE_px("/weiterbildung/" + id);

      /*let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
        // el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }*/
   }
   configHandleEvent_p() {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }
   }
}



class Detail_weit_cl {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/weiterbildung/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();





      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });

   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      var proba;
      var proba_1;
      var proba_2;
      var proba_3;
      var proba_4;
      var proba_5;
      var proba_6;
      var proba_7;
      var id;

      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if (event_opl.target.id == "speichern") {

         proba = document.getElementById("col1").value;
         proba_1 = document.getElementById("col2").value;
         proba_2 = document.getElementById("col3").value;
         proba_3 = document.getElementById("col4").value;
         proba_4 = document.getElementById("col5").value;
         proba_5 = document.getElementById("col6").value;
         proba_6 = document.getElementById("col7").value;
         proba_7 = document.getElementById("col8").value;
         id = document.getElementById("id").value;
         //var Proba=proba.concat(proba_1);
         var Proba = [id, proba, proba_1, proba_2, proba_3, proba_4, proba_5, proba_6, proba_7];
         let requester_o = new APPUTIL.Requester_cl();
         var myJSON = JSON.stringify(Proba);
         let path_s = "/weiterbildung/?data=" + myJSON;


         requester_o.PUT_px(path_s, myJSON);
         //APPUTIL.es_o.publish_px("app.cmd", ["weiterbildung", null]);
         event_opl.preventDefault();
      }
   }
}






class DetailView_cl {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/mitarbeiter/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();





      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });

   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      var proba;
      var proba_1;
      var proba_2;
      var proba_3;
      var proba_4;
      var proba_5;
      var proba_6;
      var proba_7;
      var id;

      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if (event_opl.target.id == "speichern_mit_update") {

         proba = document.getElementById("col1").value;
         proba_1 = document.getElementById("col2").value;
         proba_2 = document.getElementById("col3").value;
         proba_3 = document.getElementById("col4").value;

         id = document.getElementById("id").value;
         //var Proba=proba.concat(proba_1);
         var Proba = [id, proba, proba_1, proba_2, proba_3, proba_4, proba_5, proba_6, proba_7];
         let requester_o = new APPUTIL.Requester_cl();
         var myJSON = JSON.stringify(Proba);
         let path_s = "/mitarbeiter/?data=" + myJSON;


         requester_o.PUT_px(path_s, myJSON);
         //APPUTIL.app_o.listView_o.render_px()
        // APPUTIL.es_o.publish_px("app.cmd", ["list", null]);
         event_opl.preventDefault();
      }
   }
}


class Weiterbildung_cl {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/weiterbildung/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {





      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "Form_weit") {
         // let elx_o = document.querySelector(".notSelected");
         //if (elx_o == null) {
         // alert("Bitte zuerst einen Eintrag auswählen!");
         //} else {
         APPUTIL.es_o.publish_px("app.cmd", ["Form_weit", 0]);



         event_opl.preventDefault();
         //}
      } else if (event_opl.target.id == "update") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["detail_weit", elx_o.id]);
         }


         event_opl.preventDefault();
      } else if (event_opl.target.id == "delete_weit") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["delete_weit", elx_o.id]);
         }


         event_opl.preventDefault();
      } else if (event_opl.target.id == "qual") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["qual", elx_o.id]);
         }


         event_opl.preventDefault();
      } else if (event_opl.target.id == "qual_form") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["qual_form", elx_o.id]);
         }


         event_opl.preventDefault();
      }

   }
}

//------------------------------------------------------------------------------
class ListView_cl {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/mitarbeiter/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "Form") {
         // let elx_o = document.querySelector(".notSelected");
         //if (elx_o == null) {
         // alert("Bitte zuerst einen Eintrag auswählen!");
         //} else {
         APPUTIL.es_o.publish_px("app.cmd", ["Form", 0]);



         event_opl.preventDefault();
         //}
      } else if (event_opl.target.id == "idShowListEntry") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["detail", elx_o.id]);
         }


         event_opl.preventDefault();
      } else if (event_opl.target.id == "Weiterbildung_mit") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["Weiterbildung_mit", elx_o.id]);
         }


         event_opl.preventDefault();
      } else if (event_opl.target.id == "Anmelden") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {

            APPUTIL.es_o.publish_px("app.cmd", ["Anmelden", elx_o.id]);

         }

         event_opl.preventDefault();
      } else if (event_opl.target.id == "delete") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            let requester_o = new APPUTIL.Requester_cl();
            requester_o.DELETE_px("/mitarbeiter/" + elx_o.id);
         }


         event_opl.preventDefault();
      }


   }
}

class Weiterbildung_after {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/weiter_after/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "erfolg") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["erfolg", elx_o.id]);
            event_opl.preventDefault();
         }
      }






   }

}




class Weiterbildung_akt {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/weiter_aktiv/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "ZUM_abbrechen") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["ZUM_abbrechen", elx_o.id]);
            event_opl.preventDefault();
         }
      }






   }

}

class Abbrechen {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/erfolg/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "abbrechen") {


         let elx_o = document.querySelector(".clSelected");

         var proba = [elx_o.id, "a"]


         let requester_o = new APPUTIL.Requester_cl();
         //var myJSON = JSON.stringify(proba);
         let path_s = "/erfolg/?data=" + proba;


         requester_o.POST_px(path_s, proba);
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }





   }
}






class Stonieren {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/weit_status/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "stonieren") {


         let elx_o = document.querySelector(".clSelected");

         var proba = [elx_o.id, "s"]


         let requester_o = new APPUTIL.Requester_cl();
         //var myJSON = JSON.stringify(proba);
         let path_s = "/weit_status/?data=" + proba;


         requester_o.POST_px(path_s, proba);
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }





   }
}










class Weiterbildung_before {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/weiter_before/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "erfolg") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["erfolg", elx_o.id]);
            event_opl.preventDefault();
         }
      }






   }

}

class Erfolg {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/erfolg/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "erfolg_schiken") {


         let elx_o = document.querySelector(".clSelected");

         var proba = [elx_o.id, "e"]


         let requester_o = new APPUTIL.Requester_cl();
         //var myJSON = JSON.stringify(proba);
         let path_s = "/erfolg/?data=" + proba;


         requester_o.POST_px(path_s, proba);
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if (event_opl.target.id == "kein_erfolg") {


         let elx_o = document.querySelector(".clSelected");

         var proba = [elx_o.id, "k"]


         let requester_o = new APPUTIL.Requester_cl();
         //var myJSON = JSON.stringify(proba);
         let path_s = "/erfolg/?data=" + proba;


         requester_o.POST_px(path_s, proba);
         //APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }





   }
}



class Weiterbildung_auswertung {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/weiterbildung/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {





      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "show_before") {
         // let elx_o = document.querySelector(".notSelected");
         //if (elx_o == null) {
         // alert("Bitte zuerst einen Eintrag auswählen!");
         //} else {
         APPUTIL.es_o.publish_px("app.cmd", ["show_before", 0]);



         event_opl.preventDefault();
         //}
      } else if (event_opl.target.id == "show_after") {
         // let elx_o = document.querySelector(".notSelected");
         //if (elx_o == null) {
         // alert("Bitte zuerst einen Eintrag auswählen!");
         //} else {
         APPUTIL.es_o.publish_px("app.cmd", ["show_after", 0]);



         event_opl.preventDefault();
         //}
      } else if (event_opl.target.id == "show_akt") {
         // let elx_o = document.querySelector(".notSelected");
         //if (elx_o == null) {
         // alert("Bitte zuerst einen Eintrag auswählen!");
         //} else {
         APPUTIL.es_o.publish_px("app.cmd", ["show_akt", 0]);



         event_opl.preventDefault();
         //}
      } else if (event_opl.target.id == "Weiterbildung_mit") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["Weiterbildung_mit", elx_o.id]);
         }


         event_opl.preventDefault();
      } 


   }
}




class Erfolgreiche_Teilnehmer {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/erfolg_teil/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {





      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      }

   }
}





class Zertifikate_sort {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/zertifikate_sort/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {





      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      }

   }
}







class Hronologisch_Weit {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px(id_spl) {
      // Daten anfordern
      let path_s = "/hronologisch/" + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {





      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      }

   }
}





class Mitarbeiter_sort {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/mitarbeiter_sort/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {





      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "hronologisch") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["hronologisch", elx_o.id]);
         }


         event_opl.preventDefault();
      }

   }
}




class Weiterbildung_sort {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/weit_sort/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {





      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "erfolg_teil") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["erfolg_teil", elx_o.id]);
         }


         event_opl.preventDefault();
      }

   }
}








class Mitarbeiter_Auswertung {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px() {
      // Daten anfordern
      let path_s = "/mitarbeiter/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.GET_px(path_s)
         .then(result_spl => {
            this.doRender_p(JSON.parse(result_spl));
         })
         .catch(error_opl => {
            alert("fetch-error (get)");
         });
   }
   doRender_p(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {





      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "stonieren_page") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", ["stonieren", elx_o.id]);
         }


         event_opl.preventDefault();

      }


   }
}


//------------------------------------------------------------------------------
class SideBar_cl {
   //------------------------------------------------------------------------------

   constructor(el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px(data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p() {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p(event_opl) {
      let cmd_s = event_opl.target.dataset.action;
      APPUTIL.es_o.publish_px("app.cmd", [cmd_s, null]);
   }
}

class Application_cl {

   constructor() {
      // Registrieren zum Empfang von Nachrichten
      APPUTIL.es_o.subscribe_px(this, "templates.loaded");
      APPUTIL.es_o.subscribe_px(this, "templates.failed");
      APPUTIL.es_o.subscribe_px(this, "app.cmd");
      this.sideBar_o = new SideBar_cl("aside", "sidebar.tpl.html");
      //this.sideBar_o = new SideBar_cl("aside", "w.html");
      this.listView_o = new ListView_cl("main", "mitarbeiter.html");
      this.detailView_o = new DetailView_cl("main", "detail.tpl.html");
      this.formView_o = new FormView_cl("main", "form.tpl .html");
      this.weit_mit_View_o = new Weiterbildung_in_Mit_View_cl("main", "list.tpl.html");
      this.anmelde_View_o = new Anmelden("main", "anmeldenList.html");
      this.weiterbildung_pflege = new Weiterbildung_cl("main", "weit.html");
      this.weiterbildung_form = new FormWeiter_cl("main", "form_weiter.html");
      this.qual = new Qual("main", "QUAL.html");
      this.qual_form = new QualForm_cl("main", "qual_form.html");
      this.detail_weit = new Detail_weit_cl("main", "detail_weit.html");
      this.delete_weit_View_o = new Delete_weit_cl("main", "weiterbildung.html");
      this.weit_aus = new Weiterbildung_auswertung("main", "weit_aus.html");
      this.weit_before = new Weiterbildung_before("main", "weit_before.html");
      this.weit_akt = new Weiterbildung_akt("main", "weit_aktiv.html");
      this.weit_after = new Weiterbildung_after("main", "weit_after.html");
      this.erfolg = new Erfolg("main", "erfolg.html");
      this.abbrechen = new Abbrechen("main", "abbrechen.html");
      this.mit_aus = new Mitarbeiter_Auswertung("main", "mit_aus.html");
      this.stonieren = new Stonieren("main", "stonieren.html");
      this.auswertung_mit = new Mitarbeiter_sort("main", "mitarbeiter_sort.html");
      this.hronologisch = new Hronologisch_Weit("main", "hronologisch_weit.html");
      this.auswertung_weit = new Weiterbildung_sort("main", "weit_sort.html");
      this.erfolg_teil = new Erfolgreiche_Teilnehmer("main", "erfolg_teil.html");
      this.zertifikate_sort = new Zertifikate_sort("main", "zertifikate_sort.html");

      //this.detailView_o = new DetailView_cl("main", "w.html");
   }
   notify_px(self, message_spl, data_opl) {
      switch (message_spl) {
         case "templates.failed":
            alert("Vorlagen konnten nicht geladen werden.");
            break;
         case "templates.loaded":
            // Templates stehen zur Verfügung, Bereiche mit Inhalten füllen
            // hier zur Vereinfachung direkt
            let markup_s;
            let el_o;
            markup_s = APPUTIL.tm_o.execute_px("header.tpl.html", null);
            el_o = document.querySelector("header");
            if (el_o != null) {
               el_o.innerHTML = markup_s;
            }
            let nav_a = [
               ["home", "Startseite"],
               ["list", "Pflege Mitarbeiter"],
               ["weiterbildung", "Pflege Weiterbildung"],
               ["mitarbeiter_auswertung", "Teilnahme Mitarbeiter"],
               ["weiterbildung_auswertung", "Teilnahme Weiterbildung"],
               ["mitarbeiter_sort", "Ausnahme Mitarbeiter"],
               ["weiterbildung_sort", "Ausnahme Weiterbildung"],
               ["zertifikate_sort", "Ausnahme Zertifikate"]


            ];
            self.sideBar_o.render_px(nav_a);
            //markup_s = APPUTIL.tm_o.execute_px("home.tpl.html", [0,0]);
            APPUTIL.es_o.publish_px("app.cmd", ["home", null])
            el_o = document.querySelector("main");
            if (el_o != null) {
               el_o.innerHTML = markup_s;
            }
            break;

         case "app.cmd":
            // hier müsste man überprüfen, ob der Inhalt gewechselt werden darf
            switch (data_opl[0]) {
               case "home":
                  
                  let path_s = "/ctotal/";
                  let requester_o = new APPUTIL.Requester_cl();
                  requester_o.GET_px(path_s)
                     .then(result_spl => {
                        result_spl=(JSON.parse(result_spl));
                        let markup_s = APPUTIL.tm_o.execute_px("home.tpl.html", result_spl);
                        let el_o = document.querySelector("main");
                        if (el_o != null) {
                           el_o.innerHTML = markup_s;
                        }
                     })
                     .catch(error_opl => {
                        alert("fetch-error (get)");
                     });

                  break;
               case "list":
                  // Daten anfordern und darstellen
                  this.listView_o.render_px();
                  break;
               case "weiterbildung":
                  // Daten anfordern und darstellen
                  this.weiterbildung_pflege.render_px();
                  break;
               case "detail":
                  this.detailView_o.render_px(data_opl[1]);
                  break;
               case "idBack":
                  APPUTIL.es_o.publish_px("app.cmd", ["list", null]);
                  break;
               case "Form":
                  this.formView_o.render_px(data_opl[1]);
                  break;
               case "Form_weit":
                  this.weiterbildung_form.render_px(data_opl[1]);
                  break;
               case "Weiterbildung_mit":
                  this.weit_mit_View_o.render_px(data_opl[1]);
                  break;
               case "Anmelden":
                  this.anmelde_View_o.render_px(data_opl[1]);
                  break;
               case "qual":
                  this.qual.render_px(data_opl[1]);
                  break;
               case "qual_form":
                  this.qual_form.render_px(data_opl[1]);
                  break;
               case "detail_weit":
                  this.detail_weit.render_px(data_opl[1]);
                  break;
               case "delete_weit":
                  this.delete_weit_View_o.render_px(data_opl[1]);
                  break;
               case "weiterbildung_auswertung":
                  this.weit_aus.render_px(data_opl[1]);
                  break;
               case "show_before":
                  this.weit_before.render_px(data_opl[1]);
                  break;
               case "erfolg":
                  this.erfolg.render_px(data_opl[1]);
                  break;
               case "show_akt":
                  this.weit_akt.render_px(data_opl[1]);
                  break;
               case "ZUM_abbrechen":
                  this.abbrechen.render_px(data_opl[1]);
                  break;
               case "show_after":
                  this.weit_after.render_px(data_opl[1]);
                  break;

               case "mitarbeiter_auswertung":
                  this.mit_aus.render_px(data_opl[1]);
                  break;
               case "stonieren":
                  this.stonieren.render_px(data_opl[1]);
                  break;

               case "mitarbeiter_sort":
                  this.auswertung_mit.render_px(data_opl[1]);
                  break;
               case "hronologisch":
                  this.hronologisch.render_px(data_opl[1]);
                  break;

               case "weiterbildung_sort":
                  this.auswertung_weit.render_px(data_opl[1]);
                  break;
               case "erfolg_teil":
                  this.erfolg_teil.render_px(data_opl[1]);
                  break;
               case "zertifikate_sort":
                  this.zertifikate_sort.render_px(data_opl[1]);
                  break;





            }
            break;
      }
   }
}

window.onload = function () {
   APPUTIL.es_o = new APPUTIL.EventService_cl();
   APPUTIL.app_o = new Application_cl();
   APPUTIL.createTemplateManager_px();
}