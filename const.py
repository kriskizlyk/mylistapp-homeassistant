<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
<title>My HomeAssistant Lists</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0f1117;--bg2:#1a1d2e;--card:rgba(255,255,255,0.05);--t1:#e8e8ed;--t2:#888;--t3:#555;--bs:rgba(255,255,255,0.06);--bl:rgba(255,255,255,0.1);--g:#4CAF50;--gd:#2E7D32;--r:#FF5252}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
button{cursor:pointer}
body{font-family:'DM Sans',-apple-system,sans-serif;background:linear-gradient(145deg,var(--bg)0%,var(--bg2)50%,var(--bg)100%);color:var(--t1);min-height:100vh;-webkit-font-smoothing:antialiased}
.app{max-width:1200px;margin:0 auto;min-height:100vh;position:relative;padding:0 16px}
.hidden{display:none!important}
input,select{font-size:16px!important}
.loading{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh}
.spinner{width:36px;height:36px;border:3px solid rgba(255,255,255,0.1);border-top-color:var(--g);border-radius:50%;animation:spin .8s linear infinite}

/* Header */
.header{padding:16px 20px 12px;position:sticky;top:0;z-index:10;background:rgba(15,17,23,0.92);backdrop-filter:blur(20px);border-bottom:1px solid var(--bs);display:flex;align-items:center;justify-content:space-between;margin:0 -16px;padding-left:32px;padding-right:32px}
.logo{font-size:22px;font-weight:700;letter-spacing:-0.03em;display:flex;align-items:center;gap:10px}
.logo-icon{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;background:linear-gradient(135deg,var(--g),var(--gd));border-radius:10px;font-size:17px;font-weight:700;color:#fff}
.hdr-right{display:flex;align-items:center;gap:8px}
.back-btn{background:rgba(255,255,255,0.08);border:none;color:var(--t1);padding:8px 14px;border-radius:10px;font-size:14px;cursor:pointer;font-family:'DM Sans',sans-serif;font-weight:500}
.header-center{display:flex;align-items:center;gap:10px;min-width:0;flex:1;justify-content:center}
.header-icon-btn{font-size:24px;cursor:pointer;padding:4px 6px;border-radius:8px;background:rgba(255,255,255,0.06)}
.header-name{font-size:20px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.content{padding:16px 16px 40px}

/* Buttons */
.reorder-btn{background:rgba(255,255,255,0.08);border:1px solid var(--bl);color:#aaa;padding:6px 12px;border-radius:10px;font-size:12px;font-weight:500;cursor:pointer;font-family:'DM Sans',sans-serif}.reorder-btn.active{background:rgba(76,175,80,0.15);border-color:var(--g);color:var(--g)}
.settings-btn{display:flex;align-items:center;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:6px 10px;cursor:pointer;color:var(--t1);font-size:16px}
.trash-btn{display:flex;align-items:center;gap:4px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:6px 10px;cursor:pointer;color:#888;font-size:14px;position:relative}
.trash-badge{position:absolute;top:-4px;right:-4px;background:var(--r);color:#fff;font-size:10px;font-weight:700;width:18px;height:18px;border-radius:50%;display:flex;align-items:center;justify-content:center}

/* User bar */
.user-bar{display:flex;align-items:center;gap:12px;padding:12px 20px;background:rgba(255,255,255,0.02);border-bottom:1px solid var(--bs);overflow-x:auto;-webkit-overflow-scrolling:touch}.user-bar::-webkit-scrollbar{display:none}
.user-chip{display:flex;align-items:center;gap:8px;padding:8px 16px;border-radius:12px;cursor:pointer;white-space:nowrap;border:2px solid transparent;transition:all .2s;flex-shrink:0;background:rgba(255,255,255,0.04)}
.user-chip.active{border-color:var(--g);background:rgba(76,175,80,0.1)}
.user-chip:hover{background:rgba(255,255,255,0.08)}
.user-avatar{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:#fff;flex-shrink:0}
.user-name{font-size:14px;font-weight:600}
.user-add-chip{display:flex;align-items:center;gap:6px;padding:8px 14px;border-radius:12px;cursor:pointer;border:2px dashed rgba(255,255,255,0.15);color:#888;font-size:13px;font-weight:500;flex-shrink:0}
.user-add-chip:hover{border-color:rgba(255,255,255,0.3);color:#ccc}
.manage-users-btn{font-size:12px;color:#888;padding:6px 10px;border:1px solid rgba(255,255,255,0.08);border-radius:8px;background:rgba(255,255,255,0.04);cursor:pointer;flex-shrink:0;font-family:'DM Sans',sans-serif}

/* Grid & Cards */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px}
.section-title{font-size:14px;font-weight:700;color:#aaa;text-transform:uppercase;letter-spacing:.06em;padding:8px 4px;margin-bottom:8px;display:flex;align-items:center;gap:8px}
.card{background:var(--card);border-radius:16px;padding:20px;cursor:pointer;position:relative;overflow:hidden;animation:fadeIn .4s ease both;transition:transform .12s,box-shadow .2s}.card:hover{box-shadow:0 4px 20px rgba(0,0,0,0.3);transform:translateY(-2px)}.card:active{transform:scale(.97)}
.card-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px}.card-icon{font-size:36px}
.card-del{background:rgba(255,255,255,0.1);border:none;color:#999;width:24px;height:24px;border-radius:50%;font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center}
.card-title{font-size:15px;font-weight:600;margin-bottom:4px}.card-count{font-size:12px;color:var(--t2);margin-bottom:6px}
.card-sub{font-size:11px;font-weight:600;margin-bottom:4px}
.type-badge{display:inline-block;font-size:10px;font-weight:600;color:#aaa;border:1px solid;border-radius:6px;padding:2px 8px;margin-top:2px}
.progress-track{height:4px;background:rgba(255,255,255,0.08);border-radius:4px;overflow:hidden}.progress-track.lg{height:6px}
.progress-bar{height:100%;border-radius:4px;transition:width .4s ease}
.add-card{border:2px dashed rgba(255,255,255,0.12);background:transparent!important;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:140px}
.add-plus{font-size:32px;color:#666;font-weight:300;margin-bottom:6px}.add-text{font-size:13px;color:#666;font-weight:500}
.share-toggle{background:none;border:1px solid rgba(255,255,255,0.1);color:#888;font-size:11px;padding:3px 8px;border-radius:6px;cursor:pointer;font-family:'DM Sans',sans-serif;white-space:nowrap}.share-toggle:hover{background:rgba(255,255,255,0.06);color:#ccc}

/* Reorder */
.reorder-list{display:flex;flex-direction:column;gap:6px;-webkit-user-select:none;user-select:none;touch-action:none}
.reorder-card{display:flex;align-items:center;background:rgba(255,255,255,0.05);border-radius:14px;padding:14px 12px;gap:12px;transition:transform .15s,box-shadow .15s}
.reorder-card.dragging{background:rgba(255,255,255,0.1);box-shadow:0 8px 32px rgba(0,0,0,0.4);transform:scale(1.02);z-index:100}
.drag-handle{display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:8px;background:rgba(255,255,255,0.06);cursor:grab;flex-shrink:0;touch-action:none}
.grip-icon{font-size:20px;color:#666;line-height:1}
.reorder-name{font-size:15px;font-weight:600;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.reorder-info{font-size:12px;color:#666;flex-shrink:0}

/* List items */
.list-content-wrap{max-width:700px}
.input-row{display:flex;gap:8px;margin-bottom:16px;align-items:center}
.input-row input{flex:1;padding:14px 18px;background:rgba(255,255,255,0.06);border:1px solid var(--bl);border-radius:14px;color:var(--t1);font-family:'DM Sans',sans-serif;outline:none}
.cam-btn{width:50px;height:50px;border-radius:14px;border:1px solid var(--bl);background:rgba(255,255,255,0.06);font-size:22px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--t1)}.cam-btn:disabled{opacity:.5}
.add-btn{width:50px;height:50px;border-radius:14px;border:none;color:#fff;font-size:24px;font-weight:300;cursor:pointer;flex-shrink:0}
.pending-wrap{position:relative;margin-bottom:14px;background:rgba(255,255,255,0.04);border-radius:12px;padding:10px;display:flex;align-items:center;gap:12px}
.pending-img{width:60px;height:60px;border-radius:10px;object-fit:cover;flex-shrink:0}
.pending-del{position:absolute;top:4px;right:4px;background:rgba(255,82,82,0.9);border:none;color:#fff;width:24px;height:24px;border-radius:50%;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center}
.pending-lbl{font-size:13px;color:#888;flex:1}
.list-prog{display:flex;align-items:center;gap:12px;margin-bottom:20px}
.prog-label{font-size:13px;color:var(--t2);font-weight:600;min-width:36px;text-align:right}
.item{display:flex;align-items:center;gap:12px;padding:14px 8px;border-bottom:1px solid rgba(255,255,255,0.04)}
.item-content{flex:1;display:flex;align-items:center;gap:10px;min-width:0}
.item-text-wrap{flex:1;display:flex;flex-direction:column;gap:2px;min-width:0}
.item-thumb{width:44px;height:44px;border-radius:8px;object-fit:cover;cursor:pointer;flex-shrink:0;border:1px solid var(--bl)}
.item-time{font-size:10px;color:#666}
.cb{width:26px;height:26px;border-radius:8px;border:2px solid;background:none;cursor:pointer;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:all .2s;font-size:14px;font-weight:700;color:#fff}
.item-text{flex:1;font-size:15px;line-height:1.4;cursor:pointer;word-break:break-word}
.sub-badge{font-size:11px;color:#888;background:rgba(255,255,255,0.06);border-radius:6px;padding:2px 6px;flex-shrink:0;font-weight:600}
.expand-btn{background:none;border:none;color:var(--g);font-size:21px;cursor:pointer;padding:4px 6px;flex-shrink:0;font-weight:700}
.xfer-btn{background:none;border:none;font-size:24px;cursor:pointer;padding:4px 5px;opacity:.7;flex-shrink:0;color:#2196F3}
.del-btn{background:none;border:none;font-size:24px;cursor:pointer;padding:4px 5px;opacity:.7;flex-shrink:0;color:var(--r)}
.inline-cf{display:flex;gap:4px;flex-shrink:0}
.icf-y{background:var(--r);border:none;color:#fff;width:28px;height:28px;border-radius:7px;font-size:13px;cursor:pointer;display:flex;align-items:center;justify-content:center}
.icf-n{background:rgba(255,255,255,0.1);border:none;color:var(--t1);width:28px;height:28px;border-radius:7px;font-size:13px;cursor:pointer;display:flex;align-items:center;justify-content:center}
.comp-hdr{display:flex;justify-content:space-between;align-items:center;padding:16px 0 8px;margin-top:8px}
.comp-lbl{font-size:13px;color:#666;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.clear-btn{background:none;border:none;color:var(--r);font-size:12px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif}
.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px 20px;text-align:center}
.empty-icon{font-size:48px;margin-bottom:16px;opacity:.4}.empty-text{font-size:17px;font-weight:600;color:#666;margin-bottom:6px}.empty-sub{font-size:14px;color:var(--t3)}
.action-bar{display:flex;gap:8px;margin-top:20px;padding-top:16px;border-top:1px solid var(--bs)}
.act-btn{flex:1;padding:10px 12px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.08);border-radius:10px;color:#888;font-size:13px;font-weight:500;cursor:pointer;font-family:'DM Sans',sans-serif;display:flex;align-items:center;justify-content:center;gap:6px}

/* Sub-items */
.sub-list{margin-left:44px;padding-left:12px;border-left:2px solid rgba(255,255,255,0.06);margin-bottom:8px}
.sub-item{display:flex;align-items:center;gap:8px;padding:8px 4px;border-bottom:1px solid rgba(255,255,255,0.03)}
.sub-cb{width:18px;height:18px;border-radius:5px;border:2px solid;background:none;cursor:pointer;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:all .2s}
.sub-text-wrap{flex:1;display:flex;flex-direction:column;gap:1px;min-width:0}
.sub-text{font-size:13px;line-height:1.3;color:#ccc}
.sub-time{font-size:9px;color:#555}
.sub-thumb{width:32px;height:32px;border-radius:6px;object-fit:cover;cursor:pointer;flex-shrink:0;border:1px solid rgba(255,255,255,0.1)}
.sub-del{background:none;border:none;color:var(--r);font-size:21px;cursor:pointer;padding:2px 4px;flex-shrink:0;font-weight:700}
.sub-add-row{display:flex;gap:6px;margin-top:6px;align-items:center}
.sub-add-input{flex:1;padding:8px 12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:8px;color:var(--t1);font-size:13px;font-family:'DM Sans',sans-serif;outline:none}
.sub-cam-btn{width:32px;height:32px;border-radius:8px;border:1px solid rgba(255,255,255,0.08);background:rgba(255,255,255,0.04);font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--t1)}
.sub-add-btn{width:32px;height:32px;border-radius:8px;border:none;color:#fff;font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}

/* Modals */
.modal-ov{position:fixed;inset:0;background:rgba(0,0,0,0.7);display:flex;align-items:center;justify-content:center;z-index:50;padding:20px}
.modal{background:#1e2030;border-radius:20px;padding:24px;width:100%;max-width:440px;border:1px solid rgba(255,255,255,0.08);max-height:85vh;overflow-y:auto}
.modal-title{font-size:18px;font-weight:700;margin-bottom:16px}
.m-input{width:100%;padding:12px 16px;background:rgba(255,255,255,0.06);border:1px solid var(--bl);border-radius:12px;color:var(--t1);font-family:'DM Sans',sans-serif;outline:none;margin-bottom:16px}
.pk-label{font-size:12px;font-weight:600;color:#666;text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px}
.ic-grid{display:grid;grid-template-columns:repeat(8,1fr);gap:6px;margin-bottom:16px}
.ic-opt{width:100%;aspect-ratio:1;border:none;border-radius:10px;background:rgba(255,255,255,0.05);font-size:20px;cursor:pointer;display:flex;align-items:center;justify-content:center}.ic-opt.sel{background:rgba(255,255,255,0.15)}
.cl-grid{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px}
.cl-opt{width:28px;height:28px;border-radius:50%;border:none;cursor:pointer;transition:all .15s}.cl-opt.sel{transform:scale(1.15)}
.m-btns{display:flex;gap:10px;justify-content:flex-end}
.m-cancel{background:rgba(255,255,255,0.06);border:none;color:#999;padding:10px 20px;border-radius:10px;font-size:14px;font-weight:500;cursor:pointer;font-family:'DM Sans',sans-serif}
.m-create{border:none;color:#fff;padding:10px 24px;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif}
.pv-row{display:flex;align-items:center;gap:12px;margin-bottom:16px;padding:12px 14px;background:rgba(255,255,255,0.04);border-radius:12px}
.pv-icon{width:44px;height:44px;border-radius:12px;border:2px solid;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(255,255,255,0.05);flex-shrink:0}
.type-row{display:flex;gap:10px;margin-bottom:16px}
.type-btn{flex:1;padding:12px;background:rgba(255,255,255,0.04);border:2px solid rgba(255,255,255,0.08);border-radius:12px;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:6px;color:#888;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:600}
.type-btn.sel{border-color:var(--g);color:var(--t1);background:rgba(76,175,80,0.1)}
.img-view-wrap{position:relative;max-width:90vw;max-height:85vh}.img-view-full{max-width:100%;max-height:85vh;border-radius:16px;object-fit:contain}
.img-view-close{position:absolute;top:-12px;right:-12px;background:rgba(255,255,255,0.9);border:none;color:#333;width:32px;height:32px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-weight:700}

/* PIN */
.pin-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.85);display:flex;align-items:center;justify-content:center;z-index:100}
.pin-box{background:#1e2030;border-radius:20px;padding:32px;text-align:center;width:300px;border:1px solid rgba(255,255,255,0.08)}
.pin-avatar{width:64px;height:64px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;color:#fff;margin:0 auto 12px}
.pin-name{font-size:18px;font-weight:700;margin-bottom:4px}
.pin-sub{font-size:13px;color:#888;margin-bottom:20px}
.pin-dots{display:flex;gap:12px;justify-content:center;margin-bottom:24px}
.pin-dot{width:16px;height:16px;border-radius:50%;border:2px solid rgba(255,255,255,0.2);transition:all .2s}
.pin-dot.filled{background:var(--g);border-color:var(--g)}
.pin-dot.error{background:var(--r);border-color:var(--r)}
.pin-keypad{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;max-width:240px;margin:0 auto}
.pin-key{padding:16px;border-radius:12px;border:none;background:rgba(255,255,255,0.06);color:var(--t1);font-size:22px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif;transition:all .15s}
.pin-key:hover{background:rgba(255,255,255,0.1)}.pin-key:active{transform:scale(.95)}
.pin-key.back{font-size:16px;color:#888}
.pin-cancel{margin-top:16px;background:rgba(255,82,82,0.12);border:1px solid rgba(255,82,82,0.3);color:#FF5252;font-size:16px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif;padding:14px 0;width:100%;border-radius:12px;display:block}

/* User form */
.uf-row{margin-bottom:14px}
.uf-label{font-size:12px;font-weight:600;color:#888;text-transform:uppercase;margin-bottom:6px}
.uf-input{width:100%;padding:12px 16px;background:rgba(255,255,255,0.06);border:1px solid var(--bl);border-radius:12px;color:var(--t1);font-family:'DM Sans',sans-serif;outline:none}
.uf-pin-input{letter-spacing:12px;text-align:center;font-size:24px;font-weight:700}
.user-list-item{display:flex;align-items:center;gap:12px;padding:12px;background:rgba(255,255,255,0.04);border-radius:12px;margin-bottom:8px}
.user-list-info{flex:1;min-width:0}
.user-list-name{font-size:14px;font-weight:600}
.user-list-detail{font-size:12px;color:#888}
.user-list-actions{display:flex;gap:6px}
.ul-edit,.ul-del{border:none;padding:6px 10px;border-radius:8px;font-size:12px;cursor:pointer;font-family:'DM Sans',sans-serif;font-weight:600}
.ul-edit{background:rgba(33,150,243,0.2);color:#64B5F6}
.ul-del{background:rgba(255,82,82,0.2);color:#FF8A80}

/* Trash */
.trash-item{display:flex;align-items:center;gap:12px;padding:12px;background:rgba(255,255,255,0.04);border-radius:12px;margin-bottom:8px}
.trash-item-info{flex:1;min-width:0}
.trash-item-name{font-size:14px;font-weight:600;display:flex;align-items:center;gap:6px}
.trash-item-detail{font-size:12px;color:#888}
.trash-actions{display:flex;gap:6px}
.trash-restore{border:none;padding:6px 12px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif;background:rgba(76,175,80,0.2);color:#81C784}
.trash-perm-del{border:none;padding:6px 12px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif;background:rgba(255,82,82,0.2);color:#FF8A80}

@keyframes fadeIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
@keyframes spin{to{transform:rotate(360deg)}}
/* Mileage */
.stats-row{display:flex;gap:10px;margin-bottom:16px}.stat-card{flex:1;background:rgba(255,255,255,0.05);border-radius:12px;padding:12px 8px;text-align:center}
.stat-val{font-size:18px;font-weight:700;margin-bottom:2px}.stat-lbl{font-size:11px;color:#888;font-weight:500;text-transform:uppercase}
.mileage-add-btn{width:100%;padding:14px;border:none;border-radius:14px;color:#fff;font-size:15px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif;margin-bottom:16px}
.mileage-form{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:20px;margin-bottom:16px;animation:fadeIn .3s ease}
.mf-title{font-size:16px;font-weight:700;margin-bottom:14px}.mf-grid{display:flex;flex-direction:column;gap:12px}.mf-field{display:flex;flex-direction:column;gap:4px;flex:1}.mf-row2{display:flex;gap:10px}
.mf-label{font-size:11px;font-weight:600;color:#888;text-transform:uppercase}
.mf-input{padding:12px 14px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:10px;color:var(--t1);font-family:'DM Sans',sans-serif;outline:none;width:100%}
.mf-select{padding:12px 14px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:10px;color:var(--t1);font-family:'DM Sans',sans-serif;outline:none;width:100%;-webkit-appearance:none;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23888' d='M6 8L1 3h10z'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center;padding-right:36px}
.mf-input-row{display:flex;gap:6px;align-items:center}
.mf-auto-btn{border:none;color:#fff;width:42px;height:42px;border-radius:10px;font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.mf-loc-btn{border:1px solid rgba(255,255,255,0.1);background:rgba(255,255,255,0.06);color:#fff;width:42px;height:42px;border-radius:10px;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}.mf-loc-btn:disabled{opacity:.5}
.mf-preview{background:rgba(76,175,80,0.08);border:1px solid rgba(76,175,80,0.2);border-radius:12px;padding:12px 14px;margin-top:14px;display:flex;flex-direction:column;gap:6px}
.mf-prev-item{display:flex;justify-content:space-between}.mf-prev-lbl{font-size:13px;color:#888}.mf-prev-val{font-size:14px;font-weight:600;color:#ccc}
.mf-btns{display:flex;gap:10px;justify-content:flex-end;margin-top:16px}
.m-entry{background:rgba(255,255,255,0.04);border-radius:14px;padding:14px 16px;margin-bottom:8px}
.m-entry-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:4px}
.m-entry-date{font-size:13px;color:#888}.m-entry-station{font-size:13px;font-weight:600;color:#ccc}
.m-entry-addr{font-size:12px;color:#777;margin-bottom:6px}
.m-entry-l100{font-size:18px;font-weight:700}
.m-entry-details{display:flex;gap:10px;margin-bottom:8px;flex-wrap:wrap}.m-entry-detail{font-size:12px;color:#aaa}
.m-entry-bottom{display:flex;justify-content:space-between;align-items:center}.m-entry-odo{font-size:11px;color:#666;font-family:monospace}
.m-entry-actions{display:flex;gap:6px}
.m-entry-edit,.m-entry-del{background:none;border:none;font-size:14px;cursor:pointer;opacity:.45;padding:2px 6px;color:var(--t1)}
@media(max-width:600px){.app{padding:0}.header{margin:0;padding-left:20px;padding-right:20px}.content{padding:16px 16px 40px}.grid{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<div class="app" id="app">
<div class="loading" id="loading"><div class="spinner"></div><p style="margin-top:16px;color:#888;font-size:14px">Connecting to Home Assistant...</p></div>
<div id="main" class="hidden">
  <div id="pin-screen" class="hidden"></div>
  <div id="home-view">
    <div id="user-bar" class="user-bar"></div>
    <div class="header">
      <div class="logo"><span class="logo-icon">✓</span> My HomeAssistant Lists</div>
      <div class="hdr-right">
        <button class="reorder-btn" id="reorder-btn" onclick="toggleReorder()">↕ Reorder</button>
        <button class="trash-btn" id="trash-btn" onclick="showTrashModal()">🗑</button>
        <button class="settings-btn" onclick="showSettings()">⚙️</button>
      </div>
    </div>
    <div class="content"><div id="cat-grid"></div></div>
  </div>
  <div id="list-view" class="hidden">
    <div class="header" id="list-header"></div>
    <div class="content" id="list-content"></div>
  </div>
</div>
<div id="modals"></div>
<input type="file" id="file-input" accept="image/*" style="display:none" />
<input type="file" id="sub-file-input" accept="image/*" style="display:none" />
<input type="file" id="odo-file-input" accept="image/*" style="display:none" />
<input type="file" id="pump-file-input" accept="image/*" style="display:none" />
</div>
<script>
// === State ===
let ws=null,wsId=1,wsCbs={},state={users:[],lists:[],items:{},settings:{}};
let aCat=null,cfm=null,eiId=null,eLN=false,expanded={},subInputs={},reorder=false;
let pendingImg=null,pendingLabel="",aiLoading=false;
let subPendingImgs={},subAiLoading={},subFileTarget=null;
let activeUser=null,pinBuffer="";
let dragIdx=null,dragOverIdx=null,dragSection=null;const rowRefs=[];
let pendingDeleteListId=null,pinConfirmBuffer="";
let mfOpen=false,mfEdit=null,locLoading=false,odoLoading=false,pumpLoading=false;
let pendingOdoVal='',pendingPumpData=null;

const ICONS=["📋","📦","🏠","🎯","⭐","📌","🗂️","💼","🎒","🛠️","📝","🏗️","🛒","🔧","✈️","🏕️","🚗","🎣","⛺","🏖️","🧳","💊","🐕","🎄","🎁","🏋️","📚","🎮","🍳","🧹","🌱","⚽","⛽","🚙","🛻","🚜","🏎️","🚐","🚌","🏍️","🛵","🚲","🛞","🔩","🪛","🪚","🔨","🪜","🧰","🪣","🧲","💡","🔌","🪴","🌻","🏡","🛋️","🚿","🧺","🍽️","👶","🐱","🐾","💰","📱","💻","🎵","🎨","🏊","⛷️","🎳","🏈","🏒","⛳","🎿"];
const COLORS=["#4CAF50","#FF9800","#2196F3","#9C27B0","#E91E63","#00BCD4","#795548","#607D8B","#FF5722","#3F51B5","#009688","#F44336"];
const FSTATIONS=["","Co-op","Costco","Shell","Petro-Canada","Esso","Husky","Chevron","Canadian Tire Gas+","Pioneer","Fas Gas Plus","UFA","Domo","7-Eleven","Centex","Mobil","SuperStore","Tempo","Cango","BJ's","Flying J / Pilot","Other"];
const SERVICE_TYPES=["Oil Change","Oil & Filter Change","Tire Rotation","Tire Change (Seasonal)","Tire Balance & Alignment","New Tires","Brake Pads (Front)","Brake Pads (Rear)","Brake Rotors","Brake Fluid Flush","Transmission Fluid","Transmission Service","Coolant Flush","Power Steering Fluid","Differential Fluid","Air Filter","Cabin Air Filter","Spark Plugs","Ignition Coils","Battery Replacement","Battery Test","Alternator","Starter Motor","Serpentine Belt","Timing Belt/Chain","Water Pump","Windshield Wipers","Windshield Washer Fluid","Headlight Bulbs","Tail Light Bulbs","Wheel Bearing","CV Axle/Joint","Suspension (Shocks/Struts)","Ball Joints","Tie Rods","Exhaust/Muffler","Catalytic Converter","O2 Sensor","Fuel Filter","Fuel Injector Cleaning","Throttle Body Cleaning","A/C Recharge","A/C Compressor","Heater Core","Radiator","Thermostat","Hoses (Coolant/Heater)","Rust Proofing/Undercoating","Detail/Polish","Paint Touch-Up","Diagnostic Scan","Safety Inspection","Emission Test","Recall Service","Warranty Repair","Other"];
let svcOpen=false,svcEdit=null,vInfoOpen=false;

const $=id=>document.getElementById(id);
function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}
function fN(n,dec){dec=dec===undefined?1:dec;return isNaN(n)?"—":n.toFixed(dec)}
function fT(iso){if(!iso)return"";const d=new Date(iso),now=new Date(),diff=now-d,mins=Math.floor(diff/60000);if(mins<1)return"just now";if(mins<60)return mins+"m ago";const hrs=Math.floor(mins/60);if(hrs<24)return hrs+"h ago";const days=Math.floor(hrs/24);if(days<7)return days+"d ago";return d.toLocaleDateString([],{month:"short",day:"numeric"})+" "+d.toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"})}
function gC(id){return state.lists.find(c=>c.id===id)}
function countAll(list){let total=0,done=0;(list||[]).forEach(it=>{if(it.liters!==undefined)return;total++;if(it.done)done++;(it.subItems||[]).forEach(si=>{total++;if(si.done)done++})});return{total,done}}
function prog(id){const{total,done}=countAll(state.items[id]);return total?Math.round(done/total*100):0}
function clM(){$('modals').innerHTML=''}
function getInitials(name){return name.split(' ').map(w=>w[0]).join('').toUpperCase().substring(0,2)}
function getApiKey(){return state.settings?.anthropicKey||''}

// === HA WebSocket ===
function connectHA(){
  const proto=location.protocol==='https:'?'wss:':'ws:';
  const host=location.hostname+(location.port?':'+location.port:'');
  ws=new WebSocket(proto+'//'+host+'/api/websocket');
  let token='';
  try{if(window.parent&&window.parent.document){const ha=window.parent.document.querySelector('home-assistant');if(ha&&ha.hass)token=ha.hass.auth.data.access_token}}catch(e){}
  ws.onmessage=e=>{
    const d=JSON.parse(e.data);
    if(d.type==='auth_required')ws.send(JSON.stringify({type:'auth',access_token:token}));
    else if(d.type==='auth_ok')onConnected();
    else if(d.type==='auth_invalid')$('loading').innerHTML='<p style="color:#FF8A80;padding:20px;text-align:center">Auth failed. Reload page.</p>';
    else if(d.type==='result'&&d.id&&wsCbs[d.id]){
      if(d.success===false){console.error('WS cmd failed:',JSON.stringify(d.error));alert('Error: '+(d.error?.message||'Unknown error'));delete wsCbs[d.id];return}
      wsCbs[d.id](d.result);delete wsCbs[d.id];
    }
    else if(d.type==='event'&&d.event?.event_type==='my_lists_updated'){wsSend('my_lists/get_state',{},s=>{state=s;if(aCat)rList();else rHome()})}
  };
  ws.onerror=()=>{$('loading').innerHTML='<p style="color:#FF8A80;padding:20px;text-align:center">Connection error.<br><button onclick="location.reload()" style="background:var(--g);border:none;color:#fff;padding:8px 16px;border-radius:8px;cursor:pointer;margin-top:10px">Retry</button></p>'};
}
function wsSend(type,data,cb){const id=wsId++;if(cb)wsCbs[id]=cb;try{ws.send(JSON.stringify({id,type,...data}))}catch(e){console.error('WS send error:',e)}}
function onConnected(){
  wsSend('subscribe_events',{event_type:'my_lists_updated'});
  wsSend('my_lists/get_state',{},s=>{
    state=s||{users:[],lists:[],items:{},settings:{}};
    $('loading').classList.add('hidden');$('main').classList.remove('hidden');
    rUserBar();rHome();
    // Auto-show PIN for last remembered user
    try{const lastId=localStorage.getItem('myLists_lastUser');if(lastId){const u=(state.users||[]).find(x=>x.id===lastId);if(u){pinBuffer='';showPinScreen(u)}}}catch(e){}
  });
}

// === AI ===
function compressImg(file){return new Promise(res=>{const r=new FileReader();r.onload=e=>{const img=new Image();img.onload=()=>{const c=document.createElement('canvas');let w=img.width,h=img.height;if(w>h){if(w>800){h=(h*800)/w;w=800}}else{if(h>800){w=(w*800)/h;h=800}}c.width=w;c.height=h;c.getContext('2d').drawImage(img,0,0,w,h);res(c.toDataURL('image/jpeg',0.8))};img.src=e.target.result};r.readAsDataURL(file)})}
async function identifyImg(dataUrl){
  const key=getApiKey();if(!key)return"(set API key in Settings)";
  try{const parts=dataUrl.split(',');const mtype=parts[0].match(/data:(.*?);/)?.[1]||'image/jpeg';const b64=parts[1];
  const listName=gC(aCat)?.name||"";
  const prompt='Read all text, labels, brand names, model numbers visible. Identify the exact product or item.'+(listName?' For list "'+listName+'".':'')+' If in packaging, identify the product inside. Reply with ONLY the item name (2-10 words).';
  const r=await fetch('https://api.anthropic.com/v1/messages',{method:'POST',headers:{'Content-Type':'application/json','x-api-key':key,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},body:JSON.stringify({model:'claude-sonnet-4-20250514',max_tokens:60,messages:[{role:'user',content:[{type:'image',source:{type:'base64',media_type:mtype,data:b64}},{type:'text',text:prompt}]}]})});
  const txt=await r.text();if(!r.ok){alert('API Error '+r.status+':\n'+txt);return"(API "+r.status+")"}
  const d=JSON.parse(txt);return d.content?.[0]?.text?.trim().replace(/[.!,"']$/,'')||""
  }catch(e){alert('Error: '+e.message);return"(Error)"}
}
$('file-input').onchange=async function(e){const file=e.target.files?.[0];if(!file)return;const compressed=await compressImg(file);pendingImg=compressed;this.value='';pendingLabel="Identifying...";aiLoading=true;rList();const label=await identifyImg(compressed);pendingLabel=label;aiLoading=false;rList()};
$('sub-file-input').onchange=async function(e){const file=e.target.files?.[0];if(!file||!subFileTarget)return;const iid=subFileTarget;const compressed=await compressImg(file);subPendingImgs[iid]=compressed;this.value='';subAiLoading[iid]=true;subInputs[iid]="Identifying...";rList();const label=await identifyImg(compressed);subInputs[iid]=label;subAiLoading[iid]=false;rList()};

// AI Odometer Reader
$('odo-file-input').onchange=async function(e){
  const file=e.target.files?.[0];if(!file)return;this.value='';
  const key=getApiKey();if(!key){alert('Set API key in Settings first');return}
  odoLoading=true;rList();
  const compressed=await compressImg(file);
  try{const parts=compressed.split(',');const mtype=parts[0].match(/data:(.*?);/)?.[1]||'image/jpeg';const b64=parts[1];
  const r=await fetch('https://api.anthropic.com/v1/messages',{method:'POST',headers:{'Content-Type':'application/json','x-api-key':key,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},body:JSON.stringify({model:'claude-sonnet-4-20250514',max_tokens:30,messages:[{role:'user',content:[{type:'image',source:{type:'base64',media_type:mtype,data:b64}},{type:'text',text:'Read the odometer/trip meter from this vehicle dashboard photo. Return ONLY the number (in km or miles). No units, no text, just the number. Example: 145832'}]}]})});
  const txt=await r.text();if(!r.ok){alert('API Error '+r.status);odoLoading=false;rList();return}
  const d=JSON.parse(txt);const val=d.content?.[0]?.text?.trim().replace(/[^0-9.]/g,'')||'';
  if(val)pendingOdoVal=val;
  }catch(err){alert('Error: '+err.message)}
  odoLoading=false;rList();
};

// AI Pump Reader
$('pump-file-input').onchange=async function(e){
  const file=e.target.files?.[0];if(!file)return;this.value='';
  const key=getApiKey();if(!key){alert('Set API key in Settings first');return}
  pumpLoading=true;rList();
  const compressed=await compressImg(file);
  try{const parts=compressed.split(',');const mtype=parts[0].match(/data:(.*?);/)?.[1]||'image/jpeg';const b64=parts[1];
  const r=await fetch('https://api.anthropic.com/v1/messages',{method:'POST',headers:{'Content-Type':'application/json','x-api-key':key,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},body:JSON.stringify({model:'claude-sonnet-4-20250514',max_tokens:80,messages:[{role:'user',content:[{type:'image',source:{type:'base64',media_type:mtype,data:b64}},{type:'text',text:'Read this fuel pump display. Extract: 1) price per liter ($/L), 2) total liters pumped, 3) fuel grade/octane if visible. Return ONLY a JSON object like: {"costPerL": 1.459, "liters": 42.5, "grade": "87"} If a value is not visible, omit it. Return ONLY the JSON, no other text.'}]}]})});
  const txt=await r.text();if(!r.ok){alert('API Error '+r.status);pumpLoading=false;rList();return}
  const d=JSON.parse(txt);const raw=d.content?.[0]?.text?.trim()||'';
  try{const clean=raw.replace(/```json|```/g,'').trim();const parsed=JSON.parse(clean);
    pendingPumpData=parsed;
  }catch(err){alert('Could not read pump display. Try a clearer photo.')}
  }catch(err){alert('Error: '+err.message)}
  pumpLoading=false;rList();
};

// === WebSocket Actions ===
function createList(name,icon,color,type,shared){wsSend('my_lists/create_list',{name,icon,color,list_type:type,user_id:shared?'':activeUser?.id||'',shared:!!shared})}
function updateList(id,data){wsSend('my_lists/update_list',{list_id:id,...data})}
function deleteList(id){wsSend('my_lists/delete_list',{list_id:id})}
function reorderLists(ids){wsSend('my_lists/reorder_lists',{list_ids:ids})}
function duplicateList(id){wsSend('my_lists/duplicate_list',{list_id:id})}
function addItem(listId,text,image){const ab=activeUser?.name||'';wsSend('my_lists/add_item',{list_id:listId,text,added_by:ab,...(image?{image}:{})},()=>{wsSend('my_lists/get_state',{},s=>{state=s;rList()})})}
function toggleItem(listId,itemId){wsSend('my_lists/toggle_item',{list_id:listId,item_id:itemId})}
function deleteItem(listId,itemId){wsSend('my_lists/delete_item',{list_id:listId,item_id:itemId})}
function moveItem(from,to,id){wsSend('my_lists/move_item',{from_list:from,to_list:to,item_id:id})}
function copyItem(from,to,id){wsSend('my_lists/copy_item',{from_list:from,to_list:to,item_id:id})}
function clearDone(id){wsSend('my_lists/clear_done',{list_id:id})}
function uncheckAll(id){wsSend('my_lists/uncheck_all',{list_id:id})}
function addSubItem(listId,itemId,text,image){const ab=activeUser?.name||'';wsSend('my_lists/add_sub_item',{list_id:listId,item_id:itemId,text,added_by:ab,...(image?{image}:{})})}
function toggleSubItem(listId,itemId,subId){wsSend('my_lists/toggle_sub_item',{list_id:listId,item_id:itemId,sub_id:subId})}
function deleteSubItem(listId,itemId,subId){wsSend('my_lists/delete_sub_item',{list_id:listId,item_id:itemId,sub_id:subId})}
function toggleShared(listId,shared){wsSend('my_lists/update_list',{list_id:listId,shared:shared},()=>{wsSend('my_lists/get_state',{},s=>{state=s;rHome()})})}

// === User Bar ===
function rUserBar(){
  const ub=$('user-bar');if(!ub)return;
  const users=state.users||[];const isAdmin=activeUser&&activeUser.admin;
  let h='';
  users.forEach(u=>{
    const badge=u.admin?'<span style="font-size:9px;background:rgba(255,215,0,0.2);color:#FFD700;padding:1px 5px;border-radius:4px;font-weight:700">ADMIN</span>':'';
    h+='<div class="user-chip'+(activeUser&&activeUser.id===u.id?' active':'')+'" onclick="selectUser(\''+u.id+'\')"><div class="user-avatar" style="background:'+u.color+'">'+getInitials(u.name)+'</div><div style="display:flex;flex-direction:column;gap:2px"><span class="user-name">'+esc(u.name)+'</span>'+badge+'</div></div>';
  });
  if(isAdmin||users.length===0)h+='<div class="user-add-chip" onclick="showAddUserModal()">+ Add User</div>';
  if(activeUser&&isAdmin){
    const reqCount=(state.pinRequests||[]).length;
    h+='<button class="manage-users-btn" style="position:relative" onclick="showNotifications()">🔔'+(reqCount>0?'<span style="position:absolute;top:-4px;right:-4px;background:var(--r);color:#fff;font-size:10px;font-weight:700;width:18px;height:18px;border-radius:50%;display:flex;align-items:center;justify-content:center">'+reqCount+'</span>':'')+'</button>';
    h+='<button class="manage-users-btn" onclick="showManageUsersModal()">Manage</button>';
  }
  if(activeUser&&!isAdmin)h+='<button class="manage-users-btn" onclick="showMyProfileModal()">My Profile</button>';
  ub.innerHTML=h;
}

// === PIN ===
function selectUser(uid){
  const u=(state.users||[]).find(x=>x.id===uid);if(!u)return;
  if(activeUser&&activeUser.id===uid){activeUser=null;try{localStorage.removeItem('myLists_lastUser')}catch(e){}rUserBar();rHome();return}
  pinBuffer='';showPinScreen(u);
}
function showPinScreen(u){$('pin-screen').classList.remove('hidden');renderPin(u,false)}
function renderPin(u,error){
  const dots=[0,1,2,3].map(i=>'<div class="pin-dot'+(i<pinBuffer.length?(error?' error':' filled'):'')+'"></div>').join('');
  $('pin-screen').innerHTML='<div class="pin-overlay"><div class="pin-box"><div class="pin-avatar" style="background:'+u.color+'">'+getInitials(u.name)+'</div><div class="pin-name">'+esc(u.name)+'</div><div class="pin-sub">Enter 4-digit PIN</div><div class="pin-dots">'+dots+'</div><div class="pin-keypad">'+[1,2,3,4,5,6,7,8,9,'',0,'⌫'].map(k=>{if(k==='')return'<div></div>';if(k==='⌫')return'<button class="pin-key back" onclick="pinBack(\''+u.id+'\')">⌫</button>';return'<button class="pin-key" onclick="pinPress(\''+u.id+'\',\''+k+'\')">'+k+'</button>'}).join('')+'</div><div id="pin-msg" style="min-height:20px;margin-top:12px;font-size:13px;text-align:center"></div><button style="margin-top:4px;background:none;border:none;color:#2196F3;font-size:13px;cursor:pointer;font-family:DM Sans,sans-serif;font-weight:600" onclick="requestPinReset(\''+u.id+'\')">Forgot PIN?</button><button class="pin-cancel" onclick="cancelPin()">Cancel</button></div></div>';
}
function pinPress(uid,digit){
  const u=(state.users||[]).find(x=>x.id===uid);if(!u)return;
  pinBuffer+=digit;if(pinBuffer.length<4){renderPin(u,false);return}
  wsSend('my_lists/verify_pin',{user_id:uid,pin:pinBuffer},res=>{
    if(res.valid){activeUser=u;$('pin-screen').classList.add('hidden');pinBuffer='';try{localStorage.setItem('myLists_lastUser',uid)}catch(e){}rUserBar();rHome()}
    else{renderPin(u,true);setTimeout(()=>{pinBuffer='';renderPin(u,false)},600)}
  });
}
function pinBack(uid){const u=(state.users||[]).find(x=>x.id===uid);if(!u)return;pinBuffer=pinBuffer.slice(0,-1);renderPin(u,false)}
function cancelPin(){pinBuffer='';$('pin-screen').classList.add('hidden')}
function requestPinReset(uid){
  wsSend('my_lists/request_pin_reset',{user_id:uid},()=>{
    const msg=$('pin-msg');if(msg){msg.innerHTML='<span style="color:#4CAF50">✓ Reset request sent to admin</span>';setTimeout(()=>{if(msg)msg.innerHTML=''},3000)}
  });
}

// === PIN Delete Confirm ===
function showDeleteConfirm(listId,listName){
  if(!activeUser){alert('Select a user first');return}
  pendingDeleteListId=listId;pinConfirmBuffer='';renderDeleteConfirm(listName,false);
}
function renderDeleteConfirm(listName,error){
  const dots=[0,1,2,3].map(i=>'<div class="pin-dot'+(i<pinConfirmBuffer.length?(error?' error':' filled'):'')+'"></div>').join('');
  $('modals').innerHTML='<div class="pin-overlay"><div class="pin-box" style="border-color:rgba(255,82,82,0.2)"><div style="font-size:16px;font-weight:700;color:var(--r);margin-bottom:6px">🗑 Delete List</div><div style="font-size:13px;color:#888;margin-bottom:20px">Enter PIN to move<br><b>'+esc(listName)+'</b> to trash</div><div class="pin-dots" style="margin-bottom:20px">'+dots+'</div><div class="pin-keypad">'+[1,2,3,4,5,6,7,8,9,'',0,'⌫'].map(k=>{if(k==='')return'<div></div>';if(k==='⌫')return'<button class="pin-key back" onclick="delPinBack(\''+esc(listName)+'\')">⌫</button>';return'<button class="pin-key" onclick="delPinPress(\''+k+"','"+esc(listName)+"')\">"+k+'</button>'}).join('')+'</div><button class="pin-cancel" onclick="cancelDeleteConfirm()">Cancel</button></div></div>';
}
function delPinPress(digit,listName){
  pinConfirmBuffer+=digit;if(pinConfirmBuffer.length<4){renderDeleteConfirm(listName,false);return}
  wsSend('my_lists/delete_list_with_pin',{list_id:pendingDeleteListId,user_id:activeUser.id,pin:pinConfirmBuffer},res=>{
    if(res.success){$('modals').innerHTML='';pendingDeleteListId=null;pinConfirmBuffer='';wsSend('my_lists/get_state',{},s=>{state=s;rHome()})}
    else{renderDeleteConfirm(listName,true);setTimeout(()=>{pinConfirmBuffer='';renderDeleteConfirm(listName,false)},600)}
  });
}
function delPinBack(listName){pinConfirmBuffer=pinConfirmBuffer.slice(0,-1);renderDeleteConfirm(listName,false)}
function cancelDeleteConfirm(){$('modals').innerHTML='';pendingDeleteListId=null;pinConfirmBuffer=''}

// === Trash ===
function showTrashModal(){
  wsSend('my_lists/get_trash',{user_id:activeUser?.id||''},trash=>{
    let h='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">🗑 Trash</div>';
    if(!trash||!trash.length){h+='<div style="text-align:center;padding:30px 20px;color:#666"><p style="font-size:32px;margin-bottom:10px">🗑</p><p style="font-size:15px;font-weight:600">Trash is empty</p></div>'}
    else{trash.forEach(t=>{h+='<div class="trash-item"><span style="font-size:28px">'+t.listIcon+'</span><div class="trash-item-info"><div class="trash-item-name">'+esc(t.listName)+(t.shared?'<span style="font-size:10px;background:rgba(255,152,0,0.15);color:#FFB74D;padding:2px 6px;border-radius:4px;margin-left:6px">Shared</span>':'')+'</div><div class="trash-item-detail">'+t.itemCount+' items · '+fT(t.deletedAt)+'</div></div><div style="display:flex;gap:6px"><button class="trash-restore" onclick="restoreTrash(\''+t.id+'\')">Restore</button><button class="trash-perm-del" onclick="permDelete(\''+t.id+'\',\''+esc(t.listName)+'\')">Delete</button></div></div>'});
    h+='<button style="width:100%;padding:12px;background:rgba(255,82,82,0.1);border:1px solid rgba(255,82,82,0.2);border-radius:10px;color:#FF8A80;font-size:13px;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif;margin-top:12px" onclick="emptyTrash()">Empty Trash</button>'}
    h+='<div class="m-btns" style="margin-top:16px"><button class="m-cancel" onclick="clM()">Close</button></div></div></div>';
    $('modals').innerHTML=h;
  });
}
function restoreTrash(id){wsSend('my_lists/restore_from_trash',{trash_id:id},()=>{wsSend('my_lists/get_state',{},s=>{state=s;showTrashModal();rHome()})})}
function permDelete(id,name){if(!confirm('Permanently delete "'+name+'"?'))return;wsSend('my_lists/permanent_delete',{trash_id:id},()=>showTrashModal())}
function emptyTrash(){if(!confirm('Permanently delete everything in trash?'))return;wsSend('my_lists/empty_trash',{user_id:activeUser?.id||''},()=>showTrashModal())}

// === User Management ===
function showAddUserModal(){
  if((state.users||[]).length>0&&(!activeUser||!activeUser.admin))return;
  const uColors=["#4CAF50","#2196F3","#FF9800","#9C27B0","#E91E63","#00BCD4","#FF5722","#795548"];
  let sc=uColors[Math.floor(Math.random()*uColors.length)];window._uc=sc;
  $('modals').innerHTML='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">Add User</div><div class="uf-row"><div class="uf-label">Name</div><input class="uf-input" id="uf-name" placeholder="Enter name" /></div><div class="uf-row"><div class="uf-label">4-Digit PIN</div><input class="uf-input uf-pin-input" id="uf-pin" type="tel" maxlength="4" placeholder="• • • •" inputmode="numeric" /></div><div class="uf-row"><div class="uf-label">Email</div><input class="uf-input" id="uf-email" type="email" placeholder="email@example.com" /></div><div class="uf-row"><div class="uf-label">Phone</div><input class="uf-input" id="uf-phone" type="tel" placeholder="+1 (555) 123-4567" /></div><div class="uf-row"><div class="uf-label">Color</div><div class="cl-grid">'+uColors.map(c=>'<button class="cl-opt'+(sc===c?' sel':'')+'" style="background:'+c+';'+(sc===c?'box-shadow:0 0 0 3px #0f1117,0 0 0 5px '+c+';transform:scale(1.15)':'')+'" onclick="window._uc=\''+c+"';document.querySelectorAll('.cl-opt').forEach(b=>{b.classList.remove('sel');b.style.boxShadow='';b.style.transform=''});this.classList.add('sel');this.style.boxShadow='0 0 0 3px #0f1117,0 0 0 5px "+c+"';this.style.transform='scale(1.15)'\"></button>").join('')+'</div></div><div id="uf-err" style="color:var(--r);font-size:13px;margin-bottom:12px"></div><div class="m-btns"><button class="m-cancel" onclick="clM()">Cancel</button><button class="m-create" style="background:linear-gradient(135deg,var(--g),var(--gd))" onclick="doAddUser()">Add User</button></div></div></div>';
  $('uf-name').focus();
}
function doAddUser(){
  const name=$('uf-name')?.value?.trim(),pin=$('uf-pin')?.value?.trim(),email=$('uf-email')?.value?.trim()||'',phone=$('uf-phone')?.value?.trim()||'';
  if(!name){$('uf-err').textContent='Name is required';return}
  if(!pin||pin.length!==4||!/^\d{4}$/.test(pin)){$('uf-err').textContent='PIN must be exactly 4 digits';return}
  wsSend('my_lists/create_user',{name,pin,email,phone,color:window._uc||'#4CAF50'},()=>{clM();wsSend('my_lists/get_state',{},s=>{state=s;rUserBar();rHome()})});
}
function showManageUsersModal(){
  if(!activeUser||!activeUser.admin)return;
  const users=state.users||[];
  let h='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">Manage Users</div>';
  users.forEach(u=>{
    const ab=u.admin?'<span style="font-size:10px;background:rgba(255,215,0,0.2);color:#FFD700;padding:2px 6px;border-radius:4px;font-weight:700">Admin</span>':'';
    h+='<div class="user-list-item"><div class="user-avatar" style="background:'+u.color+';width:40px;height:40px;font-size:16px">'+getInitials(u.name)+'</div><div class="user-list-info"><div class="user-list-name">'+esc(u.name)+' '+ab+'</div><div class="user-list-detail">'+(u.email||'No email')+(u.phone?' · '+u.phone:'')+'</div></div><div class="user-list-actions"><button class="ul-edit" onclick="showEditUserModal(\''+u.id+'\')">Edit</button>'+(u.id!==activeUser.id?'<button class="ul-del" onclick="confirmDeleteUser(\''+u.id+'\',\''+esc(u.name)+'\')">Delete</button>':'')+'</div></div>';
  });
  h+='<div class="m-btns" style="margin-top:16px"><button class="m-cancel" onclick="clM()">Close</button></div></div></div>';
  $('modals').innerHTML=h;
}
function showEditUserModal(uid){
  if(!activeUser||!activeUser.admin)return;
  const u=(state.users||[]).find(x=>x.id===uid);if(!u)return;
  const uColors=["#4CAF50","#2196F3","#FF9800","#9C27B0","#E91E63","#00BCD4","#FF5722","#795548"];window._uc=u.color;
  $('modals').innerHTML='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">Edit User</div><div class="uf-row"><div class="uf-label">Name</div><input class="uf-input" id="uf-name" value="'+esc(u.name)+'" /></div><div class="uf-row"><div class="uf-label">Email</div><input class="uf-input" id="uf-email" type="email" value="'+esc(u.email||'')+'" /></div><div class="uf-row"><div class="uf-label">Phone</div><input class="uf-input" id="uf-phone" type="tel" value="'+esc(u.phone||'')+'" /></div><div class="uf-row"><div class="uf-label">Color</div><div class="cl-grid">'+uColors.map(c=>'<button class="cl-opt'+(u.color===c?' sel':'')+'" style="background:'+c+';'+(u.color===c?'box-shadow:0 0 0 3px #0f1117,0 0 0 5px '+c+';transform:scale(1.15)':'')+'" onclick="window._uc=\''+c+"';document.querySelectorAll('.cl-opt').forEach(b=>{b.classList.remove('sel');b.style.boxShadow='';b.style.transform=''});this.classList.add('sel');this.style.boxShadow='0 0 0 3px #0f1117,0 0 0 5px "+c+"';this.style.transform='scale(1.15)'\"></button>").join('')+'</div></div><div class="uf-row" style="display:flex;align-items:center;gap:10px;padding:12px;background:rgba(255,255,255,0.04);border-radius:10px"><input type="checkbox" id="uf-admin" '+(u.admin?'checked':'')+' style="width:18px;height:18px;accent-color:var(--g)" /><label for="uf-admin" style="font-size:14px;font-weight:600;color:#ccc;cursor:pointer">Admin Role</label></div><div style="padding:12px;background:rgba(255,255,255,0.04);border-radius:10px;margin-top:8px"><p style="font-size:12px;color:#888">PIN resets via 🔔 Notifications</p></div><div id="uf-err" style="color:var(--r);font-size:13px;margin-bottom:12px;margin-top:12px"></div><div class="m-btns"><button class="m-cancel" onclick="showManageUsersModal()">Back</button><button class="m-create" style="background:linear-gradient(135deg,#2196F3,#1565C0)" onclick="doEditUser(\''+u.id+'\')">Save</button></div></div></div>';
}
function doEditUser(uid){
  if(!activeUser||!activeUser.admin)return;
  const name=$('uf-name')?.value?.trim(),email=$('uf-email')?.value?.trim()||'',phone=$('uf-phone')?.value?.trim()||'',admin=$('uf-admin')?.checked||false;
  if(!name){$('uf-err').textContent='Name is required';return}
  wsSend('my_lists/update_user',{user_id:uid,name,email,phone,color:window._uc,admin},()=>{
    clM();wsSend('my_lists/get_state',{},s=>{state=s;if(activeUser&&activeUser.id===uid)activeUser={...activeUser,name,email,phone,color:window._uc,admin};rUserBar();rHome()});
  });
}
function confirmDeleteUser(uid,name){
  if(!activeUser||!activeUser.admin)return;
  if(confirm('Delete "'+name+'" and ALL their lists?')){
    wsSend('my_lists/delete_user',{user_id:uid},()=>{if(activeUser&&activeUser.id===uid){activeUser=null;try{localStorage.removeItem('myLists_lastUser')}catch(e){}}wsSend('my_lists/get_state',{},s=>{state=s;clM();rUserBar();rHome()})});
  }
}
function showMyProfileModal(){
  if(!activeUser)return;const u=activeUser;
  const uColors=["#4CAF50","#2196F3","#FF9800","#9C27B0","#E91E63","#00BCD4","#FF5722","#795548"];window._uc=u.color;
  $('modals').innerHTML='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">My Profile</div><div class="uf-row"><div class="uf-label">Name</div><input class="uf-input" id="uf-name" value="'+esc(u.name)+'" /></div><div class="uf-row"><div class="uf-label">Email</div><input class="uf-input" id="uf-email" type="email" value="'+esc(u.email||'')+'" /></div><div class="uf-row"><div class="uf-label">Phone</div><input class="uf-input" id="uf-phone" type="tel" value="'+esc(u.phone||'')+'" /></div><div class="uf-row"><div class="uf-label">Color</div><div class="cl-grid">'+uColors.map(c=>'<button class="cl-opt'+(u.color===c?' sel':'')+'" style="background:'+c+';'+(u.color===c?'box-shadow:0 0 0 3px #0f1117,0 0 0 5px '+c+';transform:scale(1.15)':'')+'" onclick="window._uc=\''+c+"';document.querySelectorAll('.cl-opt').forEach(b=>{b.classList.remove('sel');b.style.boxShadow='';b.style.transform=''});this.classList.add('sel');this.style.boxShadow='0 0 0 3px #0f1117,0 0 0 5px "+c+"';this.style.transform='scale(1.15)'\"></button>").join('')+'</div></div><div style="border-top:1px solid rgba(255,255,255,0.06);padding-top:14px;margin-top:6px"><div class="uf-label">Change PIN</div><div style="display:flex;gap:8px;margin-bottom:8px"><input class="uf-input uf-pin-input" id="uf-cur-pin" type="tel" maxlength="4" placeholder="Current" inputmode="numeric" style="flex:1;margin:0" /><input class="uf-input uf-pin-input" id="uf-new-pin" type="tel" maxlength="4" placeholder="New" inputmode="numeric" style="flex:1;margin:0" /></div></div><div id="uf-err" style="color:var(--r);font-size:13px;margin-bottom:12px"></div><div class="m-btns"><button class="m-cancel" onclick="clM()">Cancel</button><button class="m-create" style="background:linear-gradient(135deg,#2196F3,#1565C0)" onclick="doEditProfile()">Save</button></div></div></div>';
}
function doEditProfile(){
  if(!activeUser)return;
  const name=$('uf-name')?.value?.trim(),email=$('uf-email')?.value?.trim()||'',phone=$('uf-phone')?.value?.trim()||'';
  const curPin=$('uf-cur-pin')?.value?.trim()||'',newPin=$('uf-new-pin')?.value?.trim()||'';
  if(!name){$('uf-err').textContent='Name is required';return}
  if(curPin||newPin){
    if(!curPin){$('uf-err').textContent='Enter current PIN';return}
    if(!newPin||newPin.length!==4||!/^\d{4}$/.test(newPin)){$('uf-err').textContent='New PIN must be 4 digits';return}
    wsSend('my_lists/change_own_pin',{user_id:activeUser.id,current_pin:curPin,new_pin:newPin},res=>{
      if(!res.success){$('uf-err').textContent=res.error||'Failed';return}
      wsSend('my_lists/update_user',{user_id:activeUser.id,name,email,phone,color:window._uc},()=>{
        clM();wsSend('my_lists/get_state',{},s=>{state=s;activeUser={...activeUser,name,email,phone,color:window._uc};rUserBar();rHome()});
      });
    });
  }else{
    wsSend('my_lists/update_user',{user_id:activeUser.id,name,email,phone,color:window._uc},()=>{
      clM();wsSend('my_lists/get_state',{},s=>{state=s;activeUser={...activeUser,name,email,phone,color:window._uc};rUserBar();rHome()});
    });
  }
}
function showNotifications(){
  if(!activeUser||!activeUser.admin)return;
  const reqs=state.pinRequests||[];
  let h='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">🔔 Notifications</div>';
  if(!reqs.length){h+='<div style="text-align:center;padding:30px;color:#666"><p style="font-size:32px;margin-bottom:10px">✓</p><p style="font-size:15px;font-weight:600">No pending requests</p></div>'}
  else{reqs.forEach(r=>{h+='<div style="background:rgba(255,255,255,0.04);border-radius:12px;padding:14px;margin-bottom:10px;border-left:3px solid #FF9800"><div style="font-size:14px;font-weight:600;color:#ccc;margin-bottom:4px">'+esc(r.userName)+' forgot their PIN</div><div style="font-size:12px;color:#888;margin-bottom:8px">'+fT(r.createdAt)+'</div><div style="display:flex;gap:8px"><input style="flex:1;padding:10px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:8px;color:var(--t1);font-size:18px;letter-spacing:8px;text-align:center;outline:none;font-family:DM Sans,sans-serif" id="reset-pin-'+r.id+'" type="tel" maxlength="4" placeholder="PIN" inputmode="numeric" /><button style="padding:10px 16px;background:linear-gradient(135deg,var(--g),var(--gd));border:none;color:#fff;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif" onclick="doResolvePin(\''+r.id+'\')">Reset</button><button style="padding:10px 12px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.08);border-radius:8px;color:#888;font-size:13px;cursor:pointer;font-family:DM Sans,sans-serif" onclick="doDismissPin(\''+r.id+'\')">Dismiss</button></div></div>'})}
  h+='<div class="m-btns" style="margin-top:16px"><button class="m-cancel" onclick="clM()">Close</button></div></div></div>';
  $('modals').innerHTML=h;
}
function doResolvePin(reqId){const pin=$('reset-pin-'+reqId)?.value?.trim();if(!pin||pin.length!==4)return alert('Enter 4-digit PIN');wsSend('my_lists/resolve_pin_request',{request_id:reqId,new_pin:pin},()=>{wsSend('my_lists/get_state',{},s=>{state=s;showNotifications();rUserBar()})})}
function doDismissPin(reqId){wsSend('my_lists/dismiss_pin_request',{request_id:reqId},()=>{wsSend('my_lists/get_state',{},s=>{state=s;showNotifications();rUserBar()})})}

// === Rendering ===
function toggleReorder(){reorder=!reorder;$('reorder-btn').className='reorder-btn'+(reorder?' active':'');$('reorder-btn').textContent=reorder?'✓ Done':'↕ Reorder';rHome()}

function cardHTML(c,i){
  const l=state.items[c.id]||[],isM=(c.type||'standard')==='mileage',isMaint=(c.type||'standard')==='maintenance';
  const{total,done}=countAll(l);const p=isM||isMaint?0:(total?Math.round(done/total*100):0);
  const ct=isM?l.length+' entr'+(l.length===1?'y':'ies'):(isMaint?l.length+' service'+(l.length===1?'':'s'):(total?done+'/'+total+' done':'No items'));
  let msub='';if(isM&&l.length>0){let tL=0,tK=0;l.forEach(e=>{tL+=e.liters;tK+=e.curKm-e.prevKm});if(tK>0)msub='Avg: '+fN((tL/tK)*100)+' L/100km'}
  if(isMaint&&l.length>0){const totalCost=l.reduce((a,e)=>a+(e.cost||0),0);if(totalCost>0)msub='Total: $'+fN(totalCost,2)}
  const sharedBtn=c.shared?'<button class="share-toggle" onclick="event.stopPropagation();toggleShared(\''+c.id+'\',false)">📌 Shared</button>':'<button class="share-toggle" onclick="event.stopPropagation();toggleShared(\''+c.id+'\',true)">🔒 Private</button>';
  return '<div class="card" style="border-left:4px solid '+c.color+';animation-delay:'+i*.06+'s" onclick="oList(\''+c.id+'\')"><div class="card-top"><span class="card-icon">'+c.icon+'</span><div style="display:flex;gap:4px;align-items:center">'+sharedBtn+'<button class="card-del" onclick="event.stopPropagation();showDeleteConfirm(\''+c.id+'\',\''+esc(c.name)+'\')">×</button></div></div><div class="card-title">'+esc(c.name)+'</div><div class="card-count">'+ct+'</div>'+(msub?'<div class="card-sub" style="color:#4CAF50">'+msub+'</div>':'')+(!isM&&total?'<div class="progress-track"><div class="progress-bar" style="width:'+p+'%;background:'+c.color+'"></div></div>':'')+(isM?'<div class="type-badge" style="border-color:'+c.color+'">⛽ Mileage</div>':'')+(isMaint?'<div class="type-badge" style="border-color:'+c.color+'">🔧 Maintenance</div>':'')+'</div>';
}

function rHome(){
  rUserBar();
  const tb=$('trash-btn');if(tb){wsSend('my_lists/get_trash',{user_id:activeUser?.id||''},trash=>{const cnt=(trash||[]).length;tb.innerHTML='🗑'+(cnt>0?'<span class="trash-badge">'+cnt+'</span>':'')})}
  const g=$('cat-grid');
  const sharedLists=state.lists.filter(l=>l.shared);
  const userLists=activeUser?state.lists.filter(l=>l.userId===activeUser.id&&!l.shared):[];
  const allVisible=[...sharedLists,...userLists];
  const hasUsers=(state.users||[]).length>0;
  $('reorder-btn').style.display=allVisible.length>1?'inline-flex':'none';

  if(reorder){
    let h='';
    if(sharedLists.length>0){h+='<div class="section-title">📌 Shared Lists</div><div class="reorder-list">';sharedLists.forEach((c,i)=>{h+='<div class="reorder-card" data-id="'+c.id+'" data-section="shared" style="border-left:4px solid '+c.color+'"><div class="drag-handle" ontouchstart="event.preventDefault();dStart(\'shared\','+i+')" onmousedown="event.preventDefault();dStart(\'shared\','+i+')"><span class="grip-icon">⠿</span></div><span style="font-size:22px">'+c.icon+'</span><span class="reorder-name">'+esc(c.name)+'</span></div>'});h+='</div>'}
    if(activeUser&&userLists.length>0){h+='<div class="section-title" style="margin-top:16px">'+esc(activeUser.name)+'\'s Lists</div><div class="reorder-list">';userLists.forEach((c,i)=>{h+='<div class="reorder-card" data-id="'+c.id+'" data-section="user" style="border-left:4px solid '+c.color+'"><div class="drag-handle" ontouchstart="event.preventDefault();dStart(\'user\','+i+')" onmousedown="event.preventDefault();dStart(\'user\','+i+')"><span class="grip-icon">⠿</span></div><span style="font-size:22px">'+c.icon+'</span><span class="reorder-name">'+esc(c.name)+'</span></div>'});h+='</div>'}
    g.innerHTML=h;return;
  }

  let h='';
  if(sharedLists.length>0||hasUsers){h+='<div class="section-title">📌 Shared Lists</div><div class="grid">';sharedLists.forEach((c,i)=>{h+=cardHTML(c,i)});h+='<div class="card add-card" onclick="showNewListModal(true)"><span class="add-plus">+</span><p class="add-text">New Shared List</p></div></div>'}
  if(activeUser){h+='<div class="section-title" style="margin-top:20px"><span style="display:inline-block;width:24px;height:24px;border-radius:50%;background:'+activeUser.color+';text-align:center;line-height:24px;font-size:12px;font-weight:700;color:#fff;vertical-align:middle">'+getInitials(activeUser.name)+'</span> '+esc(activeUser.name)+'\'s Lists</div><div class="grid">';userLists.forEach((c,i)=>{h+=cardHTML(c,i)});h+='<div class="card add-card" onclick="showNewListModal(false)"><span class="add-plus">+</span><p class="add-text">New List</p></div></div>'}
  else if(hasUsers){h+='<div style="text-align:center;padding:40px 20px;color:#666"><p style="font-size:32px;margin-bottom:12px">👆</p><p style="font-size:16px;font-weight:600;margin-bottom:6px">Select a user above</p><p style="font-size:14px">Tap a user and enter their PIN to see their lists</p></div>'}
  if(!hasUsers&&sharedLists.length===0){h+='<div style="text-align:center;padding:60px 20px;color:#666"><p style="font-size:48px;margin-bottom:16px">👥</p><p style="font-size:17px;font-weight:600;margin-bottom:6px">Welcome to My HomeAssistant Lists</p><p style="font-size:14px;margin-bottom:20px">Add your first user to get started</p><button style="background:linear-gradient(135deg,var(--g),var(--gd));border:none;color:#fff;padding:12px 24px;border-radius:12px;font-size:15px;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif" onclick="showAddUserModal()">+ Add User</button></div>'}
  g.innerHTML=h;
}

// Drag
function dStart(section,idx){dragSection=section;dragIdx=idx;dragOverIdx=idx;document.querySelectorAll('.reorder-card[data-section="'+section+'"]').forEach((el,i)=>{if(i===idx)el.classList.add('dragging')})}
function dMove(cY){if(dragIdx===null)return;const cards=[...document.querySelectorAll('.reorder-card[data-section="'+dragSection+'"]')];for(let i=0;i<cards.length;i++){const r=cards[i].getBoundingClientRect();if(cY<r.top+r.height/2){dragOverIdx=i;return}}dragOverIdx=cards.length-1}
function dEnd(){if(dragIdx===null||dragOverIdx===null||dragIdx===dragOverIdx){dragIdx=null;dragOverIdx=null;dragSection=null;return}const cards=[...document.querySelectorAll('.reorder-card[data-section="'+dragSection+'"]')];const ids=cards.map(el=>el.getAttribute('data-id'));const[moved]=ids.splice(dragIdx,1);ids.splice(dragOverIdx,0,moved);const otherIds=state.lists.filter(l=>{if(dragSection==='shared')return !l.shared;return l.shared||l.userId!==activeUser?.id}).map(l=>l.id);let allIds;if(dragSection==='shared'){allIds=[...ids,...otherIds]}else{const sIds=state.lists.filter(l=>l.shared).map(l=>l.id);allIds=[...sIds,...ids,...state.lists.filter(l=>!l.shared&&l.userId!==activeUser?.id).map(l=>l.id)]}reorderLists(allIds);dragIdx=null;dragOverIdx=null;dragSection=null}
document.addEventListener('touchmove',e=>{if(dragIdx!==null){e.preventDefault();dMove(e.touches[0].clientY)}},{passive:false});
document.addEventListener('touchend',()=>{if(dragIdx!==null)dEnd()});
document.addEventListener('mousemove',e=>{if(dragIdx!==null){e.preventDefault();dMove(e.clientY)}});
document.addEventListener('mouseup',()=>{if(dragIdx!==null)dEnd()});

// === List View ===
function oList(id){aCat=id;cfm=null;eiId=null;eLN=false;expanded={};subInputs={};subPendingImgs={};subAiLoading={};pendingImg=null;pendingLabel='';aiLoading=false;mfOpen=false;mfEdit=null;svcOpen=false;svcEdit=null;vInfoOpen=false;$('home-view').classList.add('hidden');$('list-view').classList.remove('hidden');rList()}
function sHome(){aCat=null;$('list-view').classList.add('hidden');$('home-view').classList.remove('hidden');rHome()}
function rList(){
  const c=gC(aCat);if(!c)return;
  const h=$('list-header');
  if(eLN){
    h.innerHTML='<button class="back-btn" onclick="sHome()">← Back</button><div class="header-center"><span class="header-icon-btn" onclick="showIconModal()">'+c.icon+'</span><input class="name-edit" id="ne" value="'+esc(c.name)+'" /></div><div style="width:70px"></div>';
    const inp=$('ne');setTimeout(()=>inp&&inp.focus(),50);
    inp.onkeydown=e=>{if(e.key==='Enter')saveName();if(e.key==='Escape'){eLN=false;rList()}};
    inp.onblur=()=>saveName();
  }else{
    h.innerHTML='<button class="back-btn" onclick="sHome()">← Back</button><div class="header-center"><span class="header-icon-btn" onclick="showIconModal()">'+c.icon+'</span><span class="header-name" onclick="eLN=true;rList()">'+esc(c.name)+' <span class="edit-hint">✎</span></span></div><div style="width:70px"></div>';
  }
  const isM=(c.type||'standard')==='mileage';
  const isMaint=(c.type||'standard')==='maintenance';
  if(isM)rMileage(c);else if(isMaint)rMaintenance(c);else rStandard(c);
}
function saveName(){const inp=$('ne');if(inp&&inp.value.trim()){updateList(aCat,{name:inp.value.trim()})}eLN=false;setTimeout(()=>{wsSend('my_lists/get_state',{},s=>{state=s;rList()})},100)}
function showIconModal(){
  const c=gC(aCat);if(!c)return;let pi=c.icon,pc=c.color;
  const render=()=>{$('modals').innerHTML='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">Customize List</div><div class="pv-row" style="justify-content:center"><div class="pv-icon" style="border-color:'+pc+';width:56px;height:56px;font-size:30px">'+pi+'</div></div><div class="pk-label">ICON</div><div class="ic-grid">'+ICONS.map(i=>'<button class="ic-opt'+(pi===i?' sel':'')+'" style="'+(pi===i?'box-shadow:0 0 0 2px '+pc:'')+'" onclick="window._pi=\''+i+"';window._ri()\">"+i+'</button>').join('')+'</div><div class="pk-label">COLOR</div><div class="cl-grid">'+COLORS.map(cl=>'<button class="cl-opt'+(pc===cl?' sel':'')+'" style="background:'+cl+';'+(pc===cl?'box-shadow:0 0 0 3px #0f1117,0 0 0 5px '+cl+';transform:scale(1.15)':'')+'" onclick="window._pc=\''+cl+"';window._ri()\"></button>").join('')+'</div><div class="m-btns"><button class="m-cancel" onclick="clM()">Cancel</button><button class="m-create" style="background:linear-gradient(135deg,'+pc+','+pc+'dd)" onclick="saveIconColor()">Save</button></div></div></div>'};
  window._pi=pi;window._pc=pc;window._ri=()=>{pi=window._pi;pc=window._pc;render()};render();
}
function saveIconColor(){updateList(aCat,{icon:window._pi,color:window._pc});clM();setTimeout(()=>{wsSend('my_lists/get_state',{},s=>{state=s;rList()})},100)}

function rStandard(c){
  const ct=$('list-content'),l=state.items[aCat]||[],pn=l.filter(x=>!x.done),cp=l.filter(x=>x.done),p=prog(aCat);
  const aiLabel=pendingLabel&&!pendingLabel.startsWith('(')?pendingLabel:'';
  let s='<div class="list-content-wrap"><div class="input-row"><input type="text" id="ni" placeholder="Add an item..." '+(aiLoading?'value="Identifying..." readonly style="color:#888;font-style:italic"':(aiLabel?'value="'+esc(aiLabel)+'"':''))+' /><button class="cam-btn" onclick="document.getElementById(\'file-input\').click()" '+(aiLoading?'disabled':'')+'>'+(aiLoading?'<span style="display:inline-block;animation:spin 1s linear infinite">⟳</span>':'📷')+'</button><button class="add-btn" style="background:'+c.color+'" onclick="doAddItem()" '+(aiLoading?'disabled':'')+'>+</button></div>';
  if(pendingImg){s+='<div class="pending-wrap"><img class="pending-img" src="'+pendingImg+'" /><button class="pending-del" onclick="pendingImg=null;pendingLabel=\'\';rList()">✕</button><span class="pending-lbl">'+(aiLoading?'🤖 Identifying...':(aiLabel?'Edit if needed, tap +':'Type a name, tap +'))+'</span></div>'}
  if(l.length)s+='<div class="list-prog"><div class="progress-track lg"><div class="progress-bar" style="width:'+p+'%;background:'+c.color+'"></div></div><span class="prog-label">'+p+'%</span></div>';
  if(!l.length)s+='<div class="empty"><span class="empty-icon">'+c.icon+'</span><p class="empty-text">No items yet</p><p class="empty-sub">Add an item or snap a photo</p></div>';
  else{pn.forEach(it=>{s+=itemHTML(it,c,false)});if(cp.length){s+='<div class="comp-hdr"><span class="comp-lbl">Completed ('+cp.length+')</span><button class="clear-btn" onclick="clearDone(\''+aCat+'\')">Clear all</button></div>';cp.forEach(it=>{s+=itemHTML(it,c,true)})}s+='<div class="action-bar"><button class="act-btn" onclick="uncheckAll(\''+aCat+'\')">↩️ Uncheck All</button><button class="act-btn" onclick="duplicateList(\''+aCat+'\')">📋 Duplicate</button></div>'}
  s+='</div>';ct.innerHTML=s;
  const ni=$('ni');if(ni&&!aiLoading)ni.onkeydown=e=>{if(e.key==='Enter')doAddItem()};
}

function itemHTML(it,c,dn){
  const subs=it.subItems||[],subDone=subs.filter(s=>s.done).length,subTotal=subs.length,isExp=expanded[it.id];
  const cs=dn?'background:'+c.color+';border-color:'+c.color:'border-color:'+c.color;
  const img=it.image?'<img class="item-thumb" src="'+it.image+'" />':'';
  let meta='';if(it.createdAt||it.addedBy){const parts=[];if(it.addedBy)parts.push(esc(it.addedBy));if(it.createdAt)parts.push(fT(it.createdAt));meta='<span class="item-time">'+parts.join(' · ')+'</span>'}
  const badge=subTotal>0?'<span class="sub-badge">'+subDone+'/'+subTotal+'</span>':'';
  let h='<div class="item" style="'+(dn?'opacity:.5':'')+'"><button class="cb" style="'+cs+'" onclick="toggleItem(\''+aCat+"','"+it.id+"')\">"+(dn?'✓':'')+'</button><div class="item-content">'+img+'<div class="item-text-wrap"><span class="item-text" style="'+(dn?'text-decoration:line-through':'')+'">'+esc(it.text)+'</span>'+meta+'</div>'+badge+'</div><button class="expand-btn" onclick="expanded[\''+it.id+'\']=!expanded[\''+it.id+'\'];rList()">'+(isExp?'−':'+')+'</button>'+(dn?'':'<button class="xfer-btn" onclick="showMoveModal(\''+it.id+'\')">↗</button>')+'<button class="del-btn" onclick="deleteItem(\''+aCat+"','"+it.id+"')\">🗑</button></div>";
  if(isExp){
    h+='<div class="sub-list">';
    subs.forEach(si=>{
      const siImg=si.image?'<img class="sub-thumb" src="'+si.image+'" />':'';
      let siMeta='';if(si.createdAt||si.addedBy){const parts=[];if(si.addedBy)parts.push(esc(si.addedBy));if(si.createdAt)parts.push(fT(si.createdAt));siMeta='<span class="sub-time">'+parts.join(' · ')+'</span>'}
      h+='<div class="sub-item" style="'+(si.done?'opacity:.45':'')+'"><button class="sub-cb" style="border-color:'+c.color+';'+(si.done?'background:'+c.color:'')+'" onclick="toggleSubItem(\''+aCat+"','"+it.id+"','"+si.id+"')\">"+(si.done?'<span style="font-size:10px;color:#fff">✓</span>':'')+'</button>'+siImg+'<div class="sub-text-wrap"><span class="sub-text" style="'+(si.done?'text-decoration:line-through':'')+'">'+esc(si.text)+'</span>'+siMeta+'</div><button class="sub-del" onclick="deleteSubItem(\''+aCat+"','"+it.id+"','"+si.id+"')\">×</button></div>";
    });
    const subVal=subInputs[it.id]||'';const subLoading=subAiLoading[it.id];
    h+='<div class="sub-add-row"><input class="sub-add-input" id="si-'+it.id+'" placeholder="Add sub-item..." '+(subLoading?'value="Identifying..." readonly style="color:#888;font-style:italic"':(subVal?'value="'+esc(subVal)+'"':''))+' oninput="subInputs[\''+it.id+'\']=this.value" onkeydown="if(event.key===\'Enter\')doAddSub(\''+it.id+'\')" /><button class="sub-cam-btn" onclick="subFileTarget=\''+it.id+"';document.getElementById('sub-file-input').click()\">📷</button><button class=\"sub-add-btn\" style=\"background:"+c.color+'" onclick="doAddSub(\''+it.id+"')\">+</button></div></div>";
  }
  return h;
}

function doAddItem(){if(aiLoading)return;const t=$('ni')?.value?.trim()||'';if(!t&&!pendingImg)return;addItem(aCat,t||'Photo',pendingImg||undefined);pendingImg=null;pendingLabel='';setTimeout(()=>{wsSend('my_lists/get_state',{},s=>{state=s;rList()})},150)}
function doAddSub(iid){const text=(subInputs[iid]||'').trim();const img=subPendingImgs[iid]||null;if(!text&&!img)return;addSubItem(aCat,iid,text||'Photo',img||undefined);subInputs[iid]='';delete subPendingImgs[iid];setTimeout(()=>{wsSend('my_lists/get_state',{},s=>{state=s;rList()})},150)}
function rMileage(c){
  const ct=$('list-content'),entries=state.items[aCat]||[];
  let avgL100=0,totalL=0,totalKm=0;entries.forEach(e=>{totalL+=e.liters||0;totalKm+=(e.curKm||0)-(e.prevKm||0)});if(totalKm>0)avgL100=(totalL/totalKm)*100;
  let s='<div class="list-content-wrap">';
  // Stats
  if(entries.length>0){s+='<div class="stats-row"><div class="stat-card"><div class="stat-val">'+fN(avgL100)+'</div><div class="stat-lbl">Avg L/100km</div></div><div class="stat-card"><div class="stat-val">'+entries.length+'</div><div class="stat-lbl">Fill-ups</div></div><div class="stat-card"><div class="stat-val">'+fN(totalKm,0)+'</div><div class="stat-lbl">Total km</div></div></div>'}
  // Add button
  if(!mfOpen){s+='<button class="mileage-add-btn" style="background:'+c.color+'" onclick="openMF()">+ Add Fuel Entry</button>'}
  // Form
  if(mfOpen){
    const ed=mfEdit;const prevAuto=!ed&&entries.length>0?entries[entries.length-1].curKm:'';
    s+='<div class="mileage-form"><div class="mf-title">'+(ed?'Edit':'New')+' Fuel Entry</div>';
    // AI camera buttons
    s+='<div style="display:flex;gap:8px;margin-bottom:14px"><button style="flex:1;padding:12px;background:rgba(33,150,243,0.1);border:1px solid rgba(33,150,243,0.3);border-radius:12px;color:#64B5F6;font-size:13px;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif;display:flex;align-items:center;justify-content:center;gap:8px" onclick="document.getElementById(\'pump-file-input\').click()" '+(pumpLoading?'disabled style="flex:1;padding:12px;background:rgba(33,150,243,0.1);border:1px solid rgba(33,150,243,0.3);border-radius:12px;color:#64B5F6;font-size:13px;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif;display:flex;align-items:center;justify-content:center;gap:8px;opacity:.5"':'')+'>'+(pumpLoading?'<span style="display:inline-block;animation:spin 1s linear infinite">⟳</span> Reading...':'📷 Read Pump')+'</button>';
    s+='<button style="flex:1;padding:12px;background:rgba(76,175,80,0.1);border:1px solid rgba(76,175,80,0.3);border-radius:12px;color:#81C784;font-size:13px;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif;display:flex;align-items:center;justify-content:center;gap:8px" onclick="document.getElementById(\'odo-file-input\').click()" '+(odoLoading?'disabled style="flex:1;padding:12px;background:rgba(76,175,80,0.1);border:1px solid rgba(76,175,80,0.3);border-radius:12px;color:#81C784;font-size:13px;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif;display:flex;align-items:center;justify-content:center;gap:8px;opacity:.5"':'')+'>'+(odoLoading?'<span style="display:inline-block;animation:spin 1s linear infinite">⟳</span> Reading...':'📷 Read Odometer')+'</button></div>';
    s+='<div class="mf-grid">';
    s+='<div class="mf-field"><label class="mf-label">Date</label><input class="mf-input" type="date" id="mf-date" value="'+(ed?ed.date:new Date().toISOString().split('T')[0])+'" /></div>';
    s+='<div class="mf-row2"><div class="mf-field"><label class="mf-label">Fuel Station</label><select class="mf-select" id="mf-station"><option value="">— Select —</option>';
    FSTATIONS.filter(Boolean).forEach(st=>{s+='<option value="'+st+'"'+((ed&&ed.station===st)?' selected':'')+'>'+st+'</option>'});
    s+='</select></div><div class="mf-field"><label class="mf-label">Octane</label><select class="mf-select" id="mf-grade"><option value="">—</option><option value="87"'+(ed&&ed.grade==='87'?' selected':'')+'>87 Regular</option><option value="89"'+(ed&&ed.grade==='89'?' selected':'')+'>89 Mid-Grade</option><option value="91"'+(ed&&ed.grade==='91'?' selected':'')+'>91 Premium</option><option value="94"'+(ed&&ed.grade==='94'?' selected':'')+'>94 Super</option><option value="diesel"'+(ed&&ed.grade==='diesel'?' selected':'')+'>Diesel</option></select></div></div>';
    s+='<div class="mf-field"><label class="mf-label">Address</label><div class="mf-input-row"><input class="mf-input" style="flex:1" type="text" id="mf-address" placeholder="e.g. 123 Main St" value="'+esc(ed?ed.address||'':'')+'" /><button class="mf-loc-btn" id="loc-btn" onclick="getLoc()" '+(locLoading?'disabled':'')+'>📍</button></div></div>';
    s+='<div class="mf-row2"><div class="mf-field"><label class="mf-label">$/L</label><input class="mf-input" type="number" step="0.001" id="mf-cpl" placeholder="0.000" value="'+(ed?ed.costPerL||'':'')+'" oninput="mfCalc()" /></div><div class="mf-field"><label class="mf-label">Liters</label><input class="mf-input" type="number" step="0.01" id="mf-lit" placeholder="0.00" value="'+(ed?ed.liters||'':'')+'" oninput="mfCalc()" /></div></div>';
    s+='<div class="mf-row2"><div class="mf-field"><label class="mf-label">Current km</label><input class="mf-input" type="number" step="0.1" id="mf-cur" placeholder="0" value="'+(ed?ed.curKm||'':'')+'" oninput="mfCalc()" /></div><div class="mf-field"><label class="mf-label">Previous km</label><div class="mf-input-row"><input class="mf-input" style="flex:1" type="number" step="0.1" id="mf-prev" placeholder="0" value="'+(ed?ed.prevKm||'':prevAuto)+'" oninput="mfCalc()" />'+(entries.length>0?'<button class="mf-auto-btn" style="background:'+c.color+'" onclick="document.getElementById(\'mf-prev\').value=\''+entries[entries.length-1].curKm+'\';mfCalc()">↩</button>':'')+'</div></div></div>';
    s+='</div><div id="mf-calc"></div>';
    s+='<div class="mf-btns"><button class="m-cancel" onclick="mfOpen=false;mfEdit=null;rList()">Cancel</button><button class="m-create" style="background:linear-gradient(135deg,'+c.color+','+c.color+'dd)" onclick="saveMF()">'+(ed?'Save':'Add')+'</button></div></div>';
  }
  // Empty
  if(!entries.length&&!mfOpen){s+='<div class="empty"><span class="empty-icon">⛽</span><p class="empty-text">No entries yet</p><p class="empty-sub">Add your first fuel entry</p></div>'}
  // Entries
  [...entries].reverse().forEach(e=>{
    const dist=(e.curKm||0)-(e.prevKm||0),l100=dist>0?((e.liters||0)/dist)*100:0,cost=(e.costPerL||0)*(e.liters||0);
    s+='<div class="m-entry"><div class="m-entry-top"><div><span class="m-entry-date">'+fD(e.date)+'</span>'+(e.station?' · <span class="m-entry-station">'+esc(e.station)+'</span>':'')+(e.grade?' <span style="font-size:11px;color:#aaa;background:rgba(255,255,255,0.06);padding:1px 6px;border-radius:4px;margin-left:4px">'+esc(e.grade)+'</span>':'')+'</div><span class="m-entry-l100" style="color:'+c.color+'">'+fN(l100)+' L/100km</span></div>';
    if(e.address)s+='<div class="m-entry-addr">📍 '+esc(e.address)+'</div>';
    s+='<div class="m-entry-details"><span class="m-entry-detail">⛽ '+fN(e.liters)+'L</span>'+(e.costPerL>0?'<span class="m-entry-detail">💲'+fN(e.costPerL,3)+'/L</span>':'')+'<span class="m-entry-detail">📏 '+fN(dist,0)+' km</span>'+(cost>0?'<span class="m-entry-detail">💰 $'+fN(cost,2)+'</span>':'')+'</div>';
    s+='<div class="m-entry-bottom"><span class="m-entry-odo">'+fN(e.prevKm||0,0)+' → '+fN(e.curKm||0,0)+' km</span><div class="m-entry-actions"><button class="m-entry-edit" onclick="editMF(\''+e.id+'\')">✎</button>'+(cfm===e.id?'<div class="inline-cf"><button class="icf-y" onclick="delMF(\''+e.id+'\')">✓</button><button class="icf-n" onclick="cfm=null;rList()">✕</button></div>':'<button class="m-entry-del" onclick="cfm=\''+e.id+'\';rList()">🗑</button>')+'</div></div></div>';
  });
  if(entries.length>0){s+='<div class="action-bar"><button class="act-btn" onclick="duplicateList(\''+aCat+'\')">📋 Duplicate</button></div>'}
  s+='</div>';ct.innerHTML=s;
  if(mfOpen){
    // Apply pending AI values after render
    if(pendingOdoVal&&$('mf-cur')){$('mf-cur').value=pendingOdoVal;pendingOdoVal=''}
    if(pendingPumpData){
      if(pendingPumpData.costPerL&&$('mf-cpl'))$('mf-cpl').value=pendingPumpData.costPerL;
      if(pendingPumpData.liters&&$('mf-lit'))$('mf-lit').value=pendingPumpData.liters;
      if(pendingPumpData.grade&&$('mf-grade')){const sel=$('mf-grade');for(let i=0;i<sel.options.length;i++){if(sel.options[i].value===String(pendingPumpData.grade)){sel.selectedIndex=i;break}}}
      pendingPumpData=null;
    }
    mfCalc();
  }
}
function openMF(){mfOpen=true;mfEdit=null;pendingOdoVal='';pendingPumpData=null;rList()}
function editMF(id){const e=(state.items[aCat]||[]).find(x=>x.id===id);if(e){mfOpen=true;mfEdit=e;rList()}}
function mfCalc(){
  const lit=parseFloat($('mf-lit')?.value)||0,cur=parseFloat($('mf-cur')?.value)||0,prev=parseFloat($('mf-prev')?.value)||0,cpl=parseFloat($('mf-cpl')?.value)||0;
  const d=$('mf-calc');if(!d)return;
  if(lit>0&&cur>prev){const dist=cur-prev,l100=(lit/dist)*100,tc=cpl*lit;
    let h='<div class="mf-preview"><div class="mf-prev-item"><span class="mf-prev-lbl">Distance</span><span class="mf-prev-val">'+fN(dist,1)+' km</span></div><div class="mf-prev-item"><span class="mf-prev-lbl">Efficiency</span><span class="mf-prev-val" style="color:#4CAF50;font-weight:700">'+fN(l100)+' L/100km</span></div>';
    if(cpl>0){h+='<div class="mf-prev-item"><span class="mf-prev-lbl">Total</span><span class="mf-prev-val">$'+fN(tc,2)+'</span></div><div class="mf-prev-item"><span class="mf-prev-lbl">$/km</span><span class="mf-prev-val">$'+fN(tc/dist,3)+'</span></div>'}
    d.innerHTML=h+'</div>';
  }else{d.innerHTML=''}
}
function saveMF(){
  const date=$('mf-date')?.value,station=$('mf-station')?.value||'',grade=$('mf-grade')?.value||'',address=$('mf-address')?.value?.trim()||'';
  const cpl=parseFloat($('mf-cpl')?.value),lit=parseFloat($('mf-lit')?.value),cur=parseFloat($('mf-cur')?.value),prev=parseFloat($('mf-prev')?.value);
  if(!date){alert('Please enter a date');return}
  if(isNaN(lit)||lit<=0){alert('Please enter liters');return}
  if(isNaN(cur)||cur<=0){alert('Please enter current mileage');return}
  if(isNaN(prev)){alert('Please enter previous mileage');return}
  if(cur<=prev){alert('Current mileage must be greater than previous');return}
  const data={date,station,grade,address,costPerL:isNaN(cpl)?0:cpl,liters:lit,curKm:cur,prevKm:prev};
  if(mfEdit){
    wsSend('my_lists/update_fuel_entry',{list_id:aCat,entry_id:mfEdit.id,...data},()=>{mfOpen=false;mfEdit=null;wsSend('my_lists/get_state',{},s=>{state=s;rList()})});
  }else{
    wsSend('my_lists/add_fuel_entry',{list_id:aCat,...data},()=>{mfOpen=false;mfEdit=null;wsSend('my_lists/get_state',{},s=>{state=s;rList()})});
  }
}
function delMF(id){
  wsSend('my_lists/delete_fuel_entry',{list_id:aCat,entry_id:id},()=>{cfm=null;wsSend('my_lists/get_state',{},s=>{state=s;rList()})});
}
function getLoc(){
  if(!navigator.geolocation){$('mf-address').value='Not supported';return}
  locLoading=true;const btn=$('loc-btn');if(btn){btn.disabled=true;btn.textContent='⟳'}
  navigator.geolocation.getCurrentPosition(async pos=>{
    const{latitude:lat,longitude:lon}=pos.coords;
    try{const r=await fetch('https://nominatim.openstreetmap.org/reverse?format=json&lat='+lat+'&lon='+lon+'&zoom=18&addressdetails=1',{headers:{'Accept-Language':'en'}});
    const d=await r.json();if(d?.address){const a=d.address;const p=[a.house_number,a.road,a.city||a.town||a.village,a.state||a.province].filter(Boolean);$('mf-address').value=p.join(', ')||lat.toFixed(5)+', '+lon.toFixed(5)}
    else{$('mf-address').value=lat.toFixed(5)+', '+lon.toFixed(5)}}
    catch(e){$('mf-address').value=lat.toFixed(5)+', '+lon.toFixed(5)}
    locLoading=false;if(btn){btn.disabled=false;btn.textContent='📍'}
  },err=>{locLoading=false;if(btn){btn.disabled=false;btn.textContent='📍'}$('mf-address').value=err.code===1?'Permission denied':'Could not get location'},{enableHighAccuracy:true,timeout:10000});
}
function fD(d){if(!d)return'—';const p=d.split('-');return p[1]+'/'+p[2]+'/'+p[0]}

// === Vehicle Maintenance View ===
function rMaintenance(c){
  const ct=$('list-content'),entries=state.items[aCat]||[];
  const vi=c.vehicleInfo||{};
  const totalCost=entries.reduce((a,e)=>a+(e.cost||0),0);
  let s='<div class="list-content-wrap">';
  // Vehicle Info Card
  s+='<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:16px;margin-bottom:16px">';
  s+='<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px"><span style="font-size:14px;font-weight:700;color:#ccc">🚗 Vehicle Info</span><button style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:4px 10px;font-size:12px;color:#888;cursor:pointer;font-family:DM Sans,sans-serif" onclick="showVehicleInfoModal()">✎ Edit</button></div>';
  if(vi.year||vi.make||vi.model){
    s+='<div style="font-size:16px;font-weight:600;margin-bottom:8px">'+(vi.year?vi.year+' ':'')+(vi.make?vi.make+' ':'')+(vi.model||'')+'</div>';
  }
  const infoItems=[];
  if(vi.oilType)infoItems.push('🛢️ Oil: '+esc(vi.oilType));
  if(vi.oilCapacity)infoItems.push('📏 Capacity: '+esc(vi.oilCapacity));
  if(vi.oilFilter)infoItems.push('🔧 Filter: '+esc(vi.oilFilter));
  if(vi.tireSize)infoItems.push('🛞 Tires: '+esc(vi.tireSize));
  if(vi.tirePressure)infoItems.push('💨 PSI: '+esc(vi.tirePressure));
  if(vi.coolantType)infoItems.push('❄️ Coolant: '+esc(vi.coolantType));
  if(vi.transFluid)infoItems.push('⚙️ Trans: '+esc(vi.transFluid));
  if(vi.vin)infoItems.push('🔢 VIN: '+esc(vi.vin));
  if(vi.plate)infoItems.push('🪪 Plate: '+esc(vi.plate));
  if(infoItems.length){s+='<div style="display:flex;flex-wrap:wrap;gap:6px">'+infoItems.map(i=>'<span style="font-size:12px;color:#aaa;background:rgba(255,255,255,0.04);padding:4px 8px;border-radius:6px">'+i+'</span>').join('')+'</div>'}
  else{s+='<p style="font-size:13px;color:#666">Tap Edit to add vehicle details</p>'}
  s+='</div>';
  // Stats
  if(entries.length>0){s+='<div class="stats-row"><div class="stat-card"><div class="stat-val">'+entries.length+'</div><div class="stat-lbl">Services</div></div><div class="stat-card"><div class="stat-val">$'+fN(totalCost,0)+'</div><div class="stat-lbl">Total Cost</div></div>'+(entries.length>0&&entries[entries.length-1].mileage?'<div class="stat-card"><div class="stat-val">'+fN(entries[entries.length-1].mileage,0)+'</div><div class="stat-lbl">Last km</div></div>':'')+'</div>'}
  // Add button
  if(!svcOpen){s+='<button class="mileage-add-btn" style="background:'+c.color+'" onclick="openSvc()">+ Add Service Entry</button>'}
  // Form
  if(svcOpen){
    const ed=svcEdit;
    s+='<div class="mileage-form"><div class="mf-title">'+(ed?'Edit':'New')+' Service Entry</div><div class="mf-grid">';
    s+='<div class="mf-row2"><div class="mf-field"><label class="mf-label">Date</label><input class="mf-input" type="date" id="svc-date" value="'+(ed?ed.date:new Date().toISOString().split('T')[0])+'" /></div><div class="mf-field"><label class="mf-label">Mileage (km)</label><input class="mf-input" type="number" step="1" id="svc-km" placeholder="0" value="'+(ed?ed.mileage||'':'')+'" /></div></div>';
    s+='<div class="mf-field"><label class="mf-label">Service Type</label><select class="mf-select" id="svc-type"><option value="">— Select Service —</option>';
    SERVICE_TYPES.forEach(st=>{s+='<option value="'+st+'"'+((ed&&ed.serviceType===st)?' selected':'')+'>'+st+'</option>'});
    s+='</select></div>';
    s+='<div class="mf-row2"><div class="mf-field"><label class="mf-label">Shop / Mechanic</label><input class="mf-input" type="text" id="svc-shop" placeholder="e.g. Jiffy Lube" value="'+esc(ed?ed.shop||'':'')+'" /></div><div class="mf-field"><label class="mf-label">Cost ($)</label><input class="mf-input" type="number" step="0.01" id="svc-cost" placeholder="0.00" value="'+(ed?ed.cost||'':'')+'" /></div></div>';
    s+='<div class="mf-field"><label class="mf-label">Parts Used</label><input class="mf-input" type="text" id="svc-parts" placeholder="e.g. Mobil 1 5W-30, K&N filter" value="'+esc(ed?ed.parts||'':'')+'" /></div>';
    s+='<div class="mf-field"><label class="mf-label">Notes</label><textarea style="width:100%;padding:12px 14px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:10px;color:var(--t1);font-family:DM Sans,sans-serif;outline:none;resize:vertical;min-height:60px;font-size:14px" id="svc-notes" placeholder="Any additional notes...">'+(ed?esc(ed.notes||''):'')+'</textarea></div>';
    s+='</div><div class="mf-btns"><button class="m-cancel" onclick="svcOpen=false;svcEdit=null;rList()">Cancel</button><button class="m-create" style="background:linear-gradient(135deg,'+c.color+','+c.color+'dd)" onclick="saveSvc()">'+(ed?'Save':'Add')+'</button></div></div>';
  }
  // Empty
  if(!entries.length&&!svcOpen){s+='<div class="empty"><span class="empty-icon">🔧</span><p class="empty-text">No service records yet</p><p class="empty-sub">Add your first maintenance entry</p></div>'}
  // Entries (reverse chronological)
  [...entries].reverse().forEach(e=>{
    s+='<div class="m-entry"><div class="m-entry-top"><div><span class="m-entry-date">'+fD(e.date)+'</span>'+(e.mileage?' · <span style="font-size:12px;color:#888">'+fN(e.mileage,0)+' km</span>':'')+'</div>'+(e.cost>0?'<span style="font-size:16px;font-weight:700;color:'+c.color+'">$'+fN(e.cost,2)+'</span>':'')+'</div>';
    s+='<div style="font-size:15px;font-weight:600;margin:4px 0 6px;color:#ccc">'+esc(e.serviceType||'Service')+'</div>';
    if(e.shop)s+='<div style="font-size:12px;color:#888;margin-bottom:4px">🏪 '+esc(e.shop)+'</div>';
    if(e.parts)s+='<div style="font-size:12px;color:#888;margin-bottom:4px">🔩 '+esc(e.parts)+'</div>';
    if(e.notes)s+='<div style="font-size:12px;color:#777;margin-bottom:4px;font-style:italic">'+esc(e.notes)+'</div>';
    s+='<div class="m-entry-bottom"><span class="m-entry-odo">'+fT(e.createdAt)+'</span><div class="m-entry-actions"><button class="m-entry-edit" onclick="editSvc(\''+e.id+'\')">✎</button>'+(cfm===e.id?'<div class="inline-cf"><button class="icf-y" onclick="delSvc(\''+e.id+'\')">✓</button><button class="icf-n" onclick="cfm=null;rList()">✕</button></div>':'<button class="m-entry-del" onclick="cfm=\''+e.id+'\';rList()">🗑</button>')+'</div></div></div>';
  });
  if(entries.length>0){s+='<div class="action-bar"><button class="act-btn" onclick="duplicateList(\''+aCat+'\')">📋 Duplicate</button></div>'}
  s+='</div>';ct.innerHTML=s;
}
function openSvc(){svcOpen=true;svcEdit=null;rList()}
function editSvc(id){const e=(state.items[aCat]||[]).find(x=>x.id===id);if(e){svcOpen=true;svcEdit=e;rList()}}
function saveSvc(){
  const date=$('svc-date')?.value,serviceType=$('svc-type')?.value,km=parseFloat($('svc-km')?.value)||0;
  const shop=$('svc-shop')?.value?.trim()||'',cost=parseFloat($('svc-cost')?.value)||0;
  const parts=$('svc-parts')?.value?.trim()||'',notes=$('svc-notes')?.value?.trim()||'';
  if(!date){alert('Please enter a date');return}
  if(!serviceType){alert('Please select a service type');return}
  const data={date,serviceType,mileage:km,shop,cost,parts,notes};
  if(svcEdit){
    wsSend('my_lists/update_service_entry',{list_id:aCat,entry_id:svcEdit.id,...data},()=>{svcOpen=false;svcEdit=null;wsSend('my_lists/get_state',{},s=>{state=s;rList()})});
  }else{
    wsSend('my_lists/add_service_entry',{list_id:aCat,...data},()=>{svcOpen=false;svcEdit=null;wsSend('my_lists/get_state',{},s=>{state=s;rList()})});
  }
}
function delSvc(id){
  wsSend('my_lists/delete_service_entry',{list_id:aCat,entry_id:id},()=>{cfm=null;wsSend('my_lists/get_state',{},s=>{state=s;rList()})});
}
function showVehicleInfoModal(){
  const c=gC(aCat);if(!c)return;const vi=c.vehicleInfo||{};
  $('modals').innerHTML='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">🚗 Vehicle Info</div><div class="mf-grid"><div class="mf-row2"><div class="mf-field"><label class="mf-label">Year</label><input class="mf-input" id="vi-year" type="number" placeholder="2024" value="'+(vi.year||'')+'" /></div><div class="mf-field"><label class="mf-label">Make</label><input class="mf-input" id="vi-make" placeholder="e.g. Toyota" value="'+esc(vi.make||'')+'" /></div><div class="mf-field"><label class="mf-label">Model</label><input class="mf-input" id="vi-model" placeholder="e.g. RAV4" value="'+esc(vi.model||'')+'" /></div></div><div class="mf-row2"><div class="mf-field"><label class="mf-label">Oil Type</label><input class="mf-input" id="vi-oil" placeholder="e.g. 5W-30 Full Synthetic" value="'+esc(vi.oilType||'')+'" /></div><div class="mf-field"><label class="mf-label">Oil Capacity</label><input class="mf-input" id="vi-oilcap" placeholder="e.g. 4.7L" value="'+esc(vi.oilCapacity||'')+'" /></div></div><div class="mf-field"><label class="mf-label">Oil Filter</label><input class="mf-input" id="vi-filter" placeholder="e.g. Mobil 1 M1-108A" value="'+esc(vi.oilFilter||'')+'" /></div><div class="mf-row2"><div class="mf-field"><label class="mf-label">Tire Size</label><input class="mf-input" id="vi-tire" placeholder="e.g. 225/65R17" value="'+esc(vi.tireSize||'')+'" /></div><div class="mf-field"><label class="mf-label">Tire PSI</label><input class="mf-input" id="vi-psi" placeholder="e.g. 35" value="'+esc(vi.tirePressure||'')+'" /></div></div><div class="mf-row2"><div class="mf-field"><label class="mf-label">Coolant Type</label><input class="mf-input" id="vi-cool" placeholder="e.g. HOAT Pink" value="'+esc(vi.coolantType||'')+'" /></div><div class="mf-field"><label class="mf-label">Trans Fluid</label><input class="mf-input" id="vi-trans" placeholder="e.g. ATF WS" value="'+esc(vi.transFluid||'')+'" /></div></div><div class="mf-row2"><div class="mf-field"><label class="mf-label">VIN</label><input class="mf-input" id="vi-vin" placeholder="17 characters" value="'+esc(vi.vin||'')+'" /></div><div class="mf-field"><label class="mf-label">License Plate</label><input class="mf-input" id="vi-plate" placeholder="e.g. ABC 123" value="'+esc(vi.plate||'')+'" /></div></div></div><div class="m-btns" style="margin-top:16px"><button class="m-cancel" onclick="clM()">Cancel</button><button class="m-create" style="background:linear-gradient(135deg,#2196F3,#1565C0)" onclick="saveVehicleInfo()">Save</button></div></div></div>';
}
function saveVehicleInfo(){
  const vi={year:$('vi-year')?.value||'',make:$('vi-make')?.value?.trim()||'',model:$('vi-model')?.value?.trim()||'',oilType:$('vi-oil')?.value?.trim()||'',oilCapacity:$('vi-oilcap')?.value?.trim()||'',oilFilter:$('vi-filter')?.value?.trim()||'',tireSize:$('vi-tire')?.value?.trim()||'',tirePressure:$('vi-psi')?.value?.trim()||'',coolantType:$('vi-cool')?.value?.trim()||'',transFluid:$('vi-trans')?.value?.trim()||'',vin:$('vi-vin')?.value?.trim()||'',plate:$('vi-plate')?.value?.trim()||''};
  wsSend('my_lists/update_list',{list_id:aCat,vehicleInfo:vi},()=>{clM();wsSend('my_lists/get_state',{},s=>{state=s;rList()})});
}

// === Modals ===
function showNewListModal(shared){
  window._shared=!!shared;let si=ICONS[0],sc=COLORS[0],tp='standard';
  const title=shared?'Create Shared List':'Create New List';
  const render=()=>{const nm=$('nln')?.value||'';$('modals').innerHTML='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">'+title+'</div>'+(shared?'<div style="font-size:12px;color:#888;margin:-8px 0 16px;padding:8px 12px;background:rgba(255,255,255,0.04);border-radius:8px">📌 Visible to all users</div>':'')+'<div class="pk-label">LIST TYPE</div><div class="type-row" style="flex-wrap:wrap"><button class="type-btn'+(tp==='standard'?' sel':'')+'" onclick="window._tp=\'standard\';window._rn()"><span style="font-size:24px">📋</span>Standard</button><button class="type-btn'+(tp==='mileage'?' sel':'')+'" onclick="window._tp=\'mileage\';window._si=\'⛽\';window._sc=\'#FF9800\';window._rn()"><span style="font-size:24px">⛽</span>Mileage</button><button class="type-btn'+(tp==='maintenance'?' sel':'')+'" onclick="window._tp=\'maintenance\';window._si=\'🔧\';window._sc=\'#2196F3\';window._rn()"><span style="font-size:24px">🔧</span>Maintenance</button></div><div class="pv-row"><div class="pv-icon" style="border-color:'+sc+'">'+si+'</div><span style="font-size:16px;font-weight:600;color:#ccc">'+(esc(nm)||'List name...')+'</span></div><input class="m-input" id="nln" placeholder="List name..." value="'+esc(nm)+'" /><div class="pk-label">ICON</div><div class="ic-grid">'+ICONS.map(i=>'<button class="ic-opt'+(si===i?' sel':'')+'" style="'+(si===i?'box-shadow:0 0 0 2px '+sc:'')+'" onclick="window._si=\''+i+"';window._rn()\">"+i+'</button>').join('')+'</div><div class="pk-label">COLOR</div><div class="cl-grid">'+COLORS.map(cl=>'<button class="cl-opt'+(sc===cl?' sel':'')+'" style="background:'+cl+';'+(sc===cl?'box-shadow:0 0 0 3px #0f1117,0 0 0 5px '+cl+';transform:scale(1.15)':'')+'" onclick="window._sc=\''+cl+"';window._rn()\"></button>").join('')+'</div><div class="m-btns"><button class="m-cancel" onclick="clM()">Cancel</button><button class="m-create" style="background:linear-gradient(135deg,'+sc+','+sc+'dd)" onclick="doCreateList()">Create</button></div></div></div>';const inp=$('nln');inp?.focus();if(inp){inp.oninput=()=>{const pv=$('modals').querySelector('.pv-row span:last-child');if(pv)pv.textContent=inp.value||'List name...'};inp.onkeydown=e=>{if(e.key==='Enter')doCreateList()}}};
  window._si=si;window._sc=sc;window._tp=tp;window._rn=()=>{si=window._si;sc=window._sc;tp=window._tp;render()};render();
}
function doCreateList(){const nm=$('nln')?.value?.trim();if(!nm)return;createList(nm,window._si,window._sc,window._tp,window._shared);clM()}

function showMoveModal(iid){
  const it=(state.items[aCat]||[]).find(i=>i.id===iid);if(!it)return;
  const ot=state.lists.filter(c=>c.id!==aCat);
  $('modals').innerHTML='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">Move item to...</div><div style="padding:10px 14px;background:rgba(255,255,255,0.04);border-radius:10px;margin-bottom:16px;font-size:15px;color:#ccc">'+esc(it.text)+'</div>'+ot.map(c=>'<div style="display:flex;align-items:center;justify-content:space-between;padding:10px 12px;background:rgba(255,255,255,0.04);border-radius:10px;margin-bottom:6px"><div style="display:flex;align-items:center;gap:10px"><span style="font-size:20px">'+c.icon+'</span><span style="font-size:14px;font-weight:500">'+esc(c.name)+'</span></div><div style="display:flex;gap:6px"><button style="border:none;padding:6px 12px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;background:rgba(33,150,243,0.2);color:#64B5F6;font-family:DM Sans,sans-serif" onclick="copyItem(\''+aCat+"','"+c.id+"','"+iid+"');clM()\">Copy</button><button style=\"border:none;padding:6px 12px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;background:rgba(76,175,80,0.2);color:#81C784;font-family:DM Sans,sans-serif\" onclick=\"moveItem('"+aCat+"','"+c.id+"','"+iid+"');clM()\">Move</button></div></div>").join('')+'<button style="width:100%;padding:12px;background:rgba(255,255,255,0.06);border:none;border-radius:10px;color:#999;font-size:14px;cursor:pointer;font-family:DM Sans,sans-serif;margin-top:10px" onclick="clM()">Cancel</button></div></div>';
}

// === Settings ===
function showSettings(){
  const ak=getApiKey();
  $('modals').innerHTML='<div class="modal-ov" onclick="clM()"><div class="modal" onclick="event.stopPropagation()"><div class="modal-title">Settings</div><div class="modal-title" style="font-size:15px">💾 Backup & Restore</div><div style="display:flex;gap:8px;margin-bottom:16px"><button style="flex:1;padding:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);border-radius:12px;color:#ccc;font-size:14px;font-weight:500;cursor:pointer;font-family:DM Sans,sans-serif;display:flex;align-items:center;gap:8px;justify-content:center" onclick="doCreateBackup()"><span>💾</span> Create Backup</button><button style="flex:1;padding:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);border-radius:12px;color:#ccc;font-size:14px;font-weight:500;cursor:pointer;font-family:DM Sans,sans-serif;display:flex;align-items:center;gap:8px;justify-content:center" onclick="showBackupList()"><span>📤</span> Restore</button></div><div id="backup-status"></div><p style="font-size:11px;color:#666;margin-bottom:16px">Auto-backups every 60s. Stored in /config/custom_components/my_lists/data/backups/</p><div class="modal-title" style="font-size:15px">📷 AI Photo Recognition</div><div style="font-size:12px;margin-bottom:8px;padding:6px 10px;border-radius:8px;display:inline-block;'+(ak?'background:rgba(76,175,80,0.15);color:#81C784':'background:rgba(255,152,0,0.15);color:#FFB74D')+'">'+(ak?'✓ API key saved':'⚠ No API key set')+'</div><p class="pk-label" style="margin-top:12px">Anthropic API Key</p><input style="width:100%;padding:10px 14px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:10px;color:var(--t1);font-family:monospace;font-size:12px!important;outline:none;margin-bottom:8px" id="api-key-input" type="password" placeholder="sk-ant-..." value="'+esc(ak)+'" /><p style="font-size:11px;color:#666;margin-bottom:16px">Get your key at <b>console.anthropic.com</b></p><div id="api-save-status"></div><div class="m-btns"><button class="m-cancel" onclick="clM()">Close</button><button class="m-create" style="background:linear-gradient(135deg,#4CAF50,#2E7D32)" onclick="saveApiKey()">Save Key</button></div></div></div>';
}
function saveApiKey(){const k=$('api-key-input')?.value?.trim()||'';const st=$('api-save-status');if(st)st.innerHTML='<div style="font-size:13px;text-align:center;padding:10px;border-radius:10px;background:rgba(76,175,80,0.15);color:#81C784;margin-bottom:14px">Saving...</div>';wsSend('my_lists/set_setting',{key:'anthropicKey',value:k},()=>{state.settings.anthropicKey=k;if(st)st.innerHTML='<div style="font-size:13px;text-align:center;padding:10px;border-radius:10px;background:rgba(76,175,80,0.15);color:#81C784;margin-bottom:14px">✓ Saved!</div>';setTimeout(()=>clM(),800)})}
function doCreateBackup(){const st=$('backup-status');if(st)st.innerHTML='<div style="font-size:13px;text-align:center;padding:10px;border-radius:10px;background:rgba(76,175,80,0.15);color:#81C784;margin-bottom:14px">Saving...</div>';wsSend('my_lists/create_backup',{},()=>{if(st)st.innerHTML='<div style="font-size:13px;text-align:center;padding:10px;border-radius:10px;background:rgba(76,175,80,0.15);color:#81C784;margin-bottom:14px">✓ Backup saved!</div>';setTimeout(()=>{if($('backup-status'))$('backup-status').innerHTML=''},3000)})}
function showBackupList(){const st=$('backup-status');if(st)st.innerHTML='<div style="font-size:13px;text-align:center;padding:10px;border-radius:10px;background:rgba(76,175,80,0.15);color:#81C784;margin-bottom:14px">Loading...</div>';wsSend('my_lists/get_backups',{},backups=>{if(!backups||!backups.length){if(st)st.innerHTML='<div style="font-size:13px;text-align:center;padding:10px;border-radius:10px;background:rgba(255,82,82,0.1);color:#FF8A80;margin-bottom:14px">No backups found</div>';return}let h='<div style="max-height:300px;overflow-y:auto">';backups.forEach(b=>{const badge=b.auto?'<span style="font-size:10px;color:#888;background:rgba(255,255,255,0.06);padding:2px 6px;border-radius:4px;margin-left:6px">auto</span>':'<span style="font-size:10px;color:#4CAF50;background:rgba(76,175,80,0.1);padding:2px 6px;border-radius:4px;margin-left:6px">manual</span>';h+='<div style="background:rgba(255,255,255,0.04);border-radius:10px;margin-bottom:6px;padding:10px 12px"><div style="display:flex;align-items:center;justify-content:space-between"><div><div style="font-size:13px;font-weight:600;color:#ccc">'+fT(b.createdAt)+badge+'</div><div style="font-size:11px;color:#888">'+b.numLists+' lists, '+b.numItems+' items</div></div><button style="background:linear-gradient(135deg,#2196F3,#1565C0);border:none;color:#fff;padding:5px 10px;border-radius:6px;font-size:11px;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif" onclick="doRestoreBackup(\''+esc(b.filename)+'\')">Restore</button></div>'+(b.changes?'<div style="font-size:11px;color:#666;margin-top:6px;border-top:1px solid rgba(255,255,255,0.04);padding-top:6px">'+esc(b.changes)+'</div>':'')+'</div>'});h+='</div>';if(st)st.innerHTML=h})}
function doRestoreBackup(fn){if(!confirm('Replace ALL data with this backup?'))return;wsSend('my_lists/restore_backup',{filename:fn},res=>{if(res.success){wsSend('my_lists/get_state',{},s=>{state=s;clM();rHome()})}else alert('Failed to restore')})}

// iOS Safari fix: onclick on innerHTML-generated buttons doesn't fire reliably in iframes
// Adding ontouchstart to body tells iOS to process click events normally
document.body.setAttribute('ontouchstart','');

connectHA();
</script>
</body>
</html>
