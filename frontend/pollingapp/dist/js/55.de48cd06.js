"use strict";(self["webpackChunkpollingapp"]=self["webpackChunkpollingapp"]||[]).push([[55],{2592:function(e,t,a){a.r(t),a.d(t,{default:function(){return x}});var i=a(6190),r=a(9582),s=a(4886),n=a(4127),c=a(2827),o=a(9223),l=a(4324),u=a(9258),d=a(7808),p=function(){var e=this,t=e._self._c;return t("div",[t(n.Z,{attrs:{outlined:"",color:"success"}},[t(l.Z,{attrs:{left:""}},[e._v("mdi-account-check")]),e._v("Participantes activos")],1),t(r.Z,[t(s.EB,[t(d.Z,{attrs:{"single-line":"","hide-details":"","append-icon":"mdi-magnify",label:"Ingresa un nombre"},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}})],1)],1),t(c.Z,{attrs:{headers:e.headers,items:e.activeParticipants,search:e.search},scopedSlots:e._u([{key:"item.calificar",fn:function({item:a}){return[t(i.Z,{attrs:{color:"error"},on:{click:function(t){e.alert=!0,e.downvote(a["_id"]["$oid"],a["name"])}}},[e._v("X")])]}}])}),t(u.Z,{attrs:{color:"error"},model:{value:e.alert,callback:function(t){e.alert=t},expression:"alert"}},[e._v("Calificaste la respuesta de "+e._s(e.name)+" como incorrecta")]),t(o.Z),t(n.Z,{attrs:{outlined:"",color:"error"}},[t(l.Z,{attrs:{left:""}},[e._v("mdi-cancel")]),e._v("Participantes descalificados")],1),t(c.Z,{attrs:{headers:e.headersDesq,items:e.desqualifiedParticipants}})],1)},m=[],h=(a(7658),a(6374),a(5220)),f=a(9876),v=a(7529),Z=a(5108),g={name:"Participants",components:{Participant:v.Z},data(){return{ids:[],participants:[],alert:!1,search:"",name:"",fields:["name","questions_failed","downgrade"],headers:[{text:"Nombre",value:"name"},{text:"Seccional",value:"seccional"},{text:"Resp. incorrectas",value:"wrongQuestions"},{text:"calificar",value:"calificar"}],headersDesq:[{text:"Nombre",value:"name"},{text:"Seccional",value:"seccional"},{text:"Resp. incorrectas",value:"wrongQuestions"}]}},computed:{activeParticipants(){return this.participants.filter((e=>e.wrongQuestions<3))},desqualifiedParticipants(){return this.participants.filter((e=>e.wrongQuestions>=3))},...(0,f.rn)(h.Z,["round"])},mounted(){let e=(0,h.Z)();if(e.isAuthenticated){let t=e.getUser;this.$socket.emit("join",{room:t.id})}else this.$router.push("/login")},methods:{downvote(e,t){let a=(0,h.Z)(),i=a.getUser;this.name=t;const r=this.participants.filter((t=>t["_id"]["$oid"]==e))[0],s=new Date;let n={juror:i.id,participant_id:e,participant_name:r.name,participant_lastName:r.lastName,time:s.toString()};this.$socket.emit("downvote",n)}},sockets:{participants(e){Z.log(e),this.participants=e}},beforeDestroy(){let e=(0,h.Z)(),t=e.getUser;this.$socket.emit("leave",{room:t.id})}},_=g,k=a(1001),w=(0,k.Z)(_,p,m,!1,null,null,null),x=w.exports}}]);
//# sourceMappingURL=55.de48cd06.js.map