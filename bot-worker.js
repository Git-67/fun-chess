importScripts('engine.js?v=3');
onmessage=e=>{postMessage(Chaos.bot(e.data.state,e.data.level,e.data.level==='hard'?850:450))};
