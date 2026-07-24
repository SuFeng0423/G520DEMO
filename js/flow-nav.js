/**
 * 流程串联：眼镜端（拍一张即传）→ APK 端
 */
(function () {
  const params = new URLSearchParams(location.search);
  let flow = params.get('flow');
  if (flow === 'full' || flow === 'glasses' || flow === 'apk' || flow === 'basic') {
    localStorage.setItem('deom-flow', flow === 'basic' ? 'full' : flow);
  } else {
    flow = localStorage.getItem('deom-flow') || 'full';
  }

  const FLOWS = {
    full: [
      { file: '01-login.html', label: '登录' },
      { file: '02-work-order-list.html', label: '选工单' },
      { file: '03-work-order-confirm.html', label: '确认' },
      { file: '04-inspection-preview-on.html', label: '拍照' },
      { file: '05-inspection-preview-off.html', label: '预览关' },
      { file: '06-auto-sync-toast.html', label: '自动同步' },
      { file: '01-gallery.html', label: 'APK相册' },
      { file: '02-preview.html', label: '预览' },
      { file: '03-delete.html', label: '删图' },
      { file: '04-submit-progress.html', label: '提交' },
      { file: '05-submit-done.html', label: '归档' },
    ],
    glasses: [
      { file: '01-login.html', label: '登录' },
      { file: '02-work-order-list.html', label: '选工单' },
      { file: '03-work-order-confirm.html', label: '确认' },
      { file: '04-inspection-preview-on.html', label: '拍照' },
      { file: '05-inspection-preview-off.html', label: '预览关' },
      { file: '06-auto-sync-toast.html', label: '自动同步' },
      { file: '08-task-end.html', label: '结束' },
    ],
    apk: [
      { file: '01-gallery.html', label: '相册' },
      { file: '02-preview.html', label: '预览' },
      { file: '03-delete.html', label: '删图' },
      { file: '04-submit-progress.html', label: '提交' },
      { file: '05-submit-done.html', label: '归档' },
    ],
  };

  window.DEOM_FLOW = flow;

  function currentFile() {
    return location.pathname.split('/').pop().split('?')[0];
  }

  function indexHref() {
    const path = location.pathname.replace(/\\/g, '/');
    if (path.includes('/screens/apk/')) return '../../index.html';
    if (path.includes('/screens/')) return '../index.html';
    return 'index.html';
  }

  function renderFlowBar() {
    const steps = FLOWS[flow] || FLOWS.full;
    const file = currentFile();
    let idx = steps.findIndex((s) => s.file === file);
    if (idx < 0) return;

    const bar = document.createElement('div');
    bar.className = 'flow-walkthrough';
    bar.innerHTML =
      '<div class="flow-walkthrough__head">' +
      '<span class="flow-walkthrough__badge">三端流程</span>' +
      '<span class="flow-walkthrough__progress">步骤 ' +
      (idx + 1) +
      ' / ' +
      steps.length +
      '</span>' +
      '<a class="flow-walkthrough__home" href="' +
      indexHref() +
      '">流程总览</a>' +
      '</div>' +
      '<div class="flow-walkthrough__steps">' +
      steps
        .map(function (s, i) {
          var cls = 'flow-walkthrough__step';
          if (i === idx) cls += ' flow-walkthrough__step--active';
          else if (i < idx) cls += ' flow-walkthrough__step--done';
          return '<span class="' + cls + '">' + s.label + '</span>';
        })
        .join('<span class="flow-walkthrough__arrow">→</span>') +
      '</div>';
    document.body.insertBefore(bar, document.body.firstChild);
  }

  document.addEventListener('DOMContentLoaded', function () {
    renderFlowBar();
  });
})();
