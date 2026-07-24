/**
 * 流程串联：?flow=basic，localStorage 记忆，自动修正分支导航
 */
(function () {
  const params = new URLSearchParams(location.search);
  let flow = params.get('flow');
  if (flow === 'basic') {
    localStorage.setItem('deom-flow', flow);
  } else {
    flow = localStorage.getItem('deom-flow') || 'basic';
  }

  const STEPS = [
    { file: '01-login.html', label: '登录' },
    { file: '02-work-order-list.html', label: '选工单' },
    { file: '03-work-order-confirm.html', label: '确认作业' },
    { file: '04-inspection-preview-on.html', label: '预览开' },
    { file: '05-inspection-preview-off.html', label: '预览关' },
    { file: '06-photo-review.html', label: '照片回看' },
    { file: '07-upload-match-success.html', label: '上传留档' },
    { file: '09-upload-complete.html', label: '上传完成' },
    { file: '10-task-end.html', label: '结束任务' },
  ];

  window.DEOM_FLOW = flow;

  function currentFile() {
    return location.pathname.split('/').pop().split('?')[0];
  }

  function indexHref() {
    const path = location.pathname.replace(/\\/g, '/');
    if (path.includes('/screens/')) return '../index.html';
    return 'index.html';
  }

  function renderFlowBar() {
    const file = currentFile();
    let idx = STEPS.findIndex((s) => s.file === file);
    if (idx < 0) return;

    const bar = document.createElement('div');
    bar.className = 'flow-walkthrough';
    bar.innerHTML =
      '<div class="flow-walkthrough__head">' +
      '<span class="flow-walkthrough__badge">流程体验</span>' +
      '<span class="flow-walkthrough__progress">步骤 ' +
      (idx + 1) +
      ' / ' +
      STEPS.length +
      '</span>' +
      '<a class="flow-walkthrough__home" href="' +
      indexHref() +
      '">流程总览</a>' +
      '</div>' +
      '<div class="flow-walkthrough__steps">' +
      STEPS.map(function (s, i) {
        var cls = 'flow-walkthrough__step';
        if (i === idx) cls += ' flow-walkthrough__step--active';
        else if (i < idx) cls += ' flow-walkthrough__step--done';
        return '<span class="' + cls + '">' + s.label + '</span>';
      }).join('<span class="flow-walkthrough__arrow">→</span>') +
      '</div>';
    document.body.insertBefore(bar, document.body.firstChild);
  }

  document.addEventListener('DOMContentLoaded', function () {
    renderFlowBar();
  });
})();
