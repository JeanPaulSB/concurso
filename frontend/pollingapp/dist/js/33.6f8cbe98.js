"use strict";(self["webpackChunkpollingapp"]=self["webpackChunkpollingapp"]||[]).push([[33],{7033:function(t,a,i){i.r(a),i.d(a,{default:function(){return h}});var n=function(){var t=this,a=t._self._c;return a("div",{staticClass:"participants-container"},t._l(t.participants,(function(i){return a("b-card",{staticClass:"w-25 mt-2",attrs:{"bg-variant":"dark","text-variant":"white",title:i.name}},[a("b-card-text",[t._v(t._s(i.name)+" "+t._s(i.lastName))]),a("b-card-text",[a("a",{attrs:{href:"http://127.0.0.1:5000/participant/"+i["$oid"]}},[t._v(t._s(i["$oid"]))])])],1)})),1)},s=[],r=(i(7658),i(6374)),e=i(5220),p=i(772),c=i(1393),l={name:"Participants",components:{BCard:p._,BCardText:c.j},data(){return{ids:[],participants:[]}},mounted(){let t=(0,e.Z)();console.log("we are loading your participants, just wait..."),r.Z.jurorParticipants(t.getUser.id).then((t=>{this.ids=t.data[0]["participants"],console.log(this.ids);for(let a=0;a<this.ids.length;a++)r.Z.participant(this.ids[a]["$oid"]).then((t=>{this.participants.push(t.data)}))}))}},o=l,d=i(1001),u=(0,d.Z)(o,n,s,!1,null,null,null),h=u.exports}}]);
//# sourceMappingURL=33.6f8cbe98.js.map