var sortable = new Sortable(el, {
    group: "name",  // or { name: "...", pull: [true, false, 'clone', array], put: [true, false, array] }
    sort: true,  // boolean 定义是否列表单元是否可以在列表容器内进行拖拽排序
    delay: 0, // number 定义鼠标选中列表单元可以开始拖动的延迟时间；
    touchStartThreshold: 0, // px, 在取消延迟的拖动事件之前，该点应该移动多少像素
    disabled: false, // boolean 定义是否此sortable对象是否可用，为true时sortable对象不能拖放排序等功能，为false时为可以进行排序，相当于一个开关；
    store: null,  // @see Store
    animation: 150,  // ms, number 单位：ms，定义排序动画的时间
    easing: "cubic-bezier(1, 0, 0, 1)", // 宽松的动画。默认为空。有关示例，请参见https://easings.net/。
    handle: ".my-handle",  // 格式为简单css选择器的字符串，使列表单元中符合选择器的元素成为拖动的手柄，只有按住拖动手柄才能使列表单元进行拖动
    filter: ".ignore-elements",  // 过滤器，不需要进行拖动的元素
    preventOnFilter: true, //  在触发过滤器`filter`的时候调用`event.preventDefault()`
    draggable: ".item",  // 允许拖拽的项目类名
    ghostClass: "sortable-ghost",  // drop placeholder的css类名
    chosenClass: "sortable-chosen",  // 被选中项的css 类名
    dragClass: "sortable-drag",  // 正在被拖拽中的css类名
    dataIdAttr: 'data-id',

    swapThreshold: 1, // 交换区域的阈值
    invertSwap: false, // 如果设置为真，是否总是使用反向交换区
    invertedSwapThreshold: 1, // 反转互换区域的阈值(默认设置为swapThreshold值)
    direction: 'horizontal', // 拖拽方向 (默认情况下会自动判断方向)

    forceFallback: false,  // 忽略 HTML5拖拽行为，强制回调进行

    fallbackClass: "sortable-fallback",  // 当使用forceFallback的时候，被复制的dom的css类名
    fallbackOnBody: false,  // 将cloned DOM 元素挂到body元素上。
    fallbackTolerance: 0, // 以像素为单位指定鼠标在被视为拖动之前应该移动的距离。
    scroll: true, // or HTMLElement
    scrollFn: function(offsetX, offsetY, originalEvent, touchEvt, hoverTargetEl) { 
        
     }, // 如果您有自定义滚动条，可以使用scrollFn进行自动滚动
    scrollSensitivity: 30, // px, 鼠标必须离边缘多近才能开始滚动。
    scrollSpeed: 10, // px
    bubbleScroll: true, // 将autoscroll应用于所有父元素，以便更轻松地移动

    dragoverBubble: false,
    removeCloneOnHide: true, // 当克隆元素不显示时删除它，而不是仅仅隐藏它
    emptyInsertThreshold: 5, // px, 距离鼠标必须从空可排序插入拖动元素到它


    setData: function (/** DataTransfer */dataTransfer, /** HTMLElement*/dragEl) {
        dataTransfer.setData('Text', dragEl.textContent); // ' dataTransfer '对象的HTML5 DragEvent
    },

    // 元素被选中
    onChoose: function (/**Event*/evt) {
        evt.oldIndex;  // 父元素索引
    },

    // 元素未被选中的时候（从选中到未选中）
    onUnchoose: function(/**Event*/evt) {
        // 与onEnd相同的属性
    },

    // 开始拖拽的时候
    onStart: function (/**Event*/evt) {
        evt.oldIndex;  // 父元素索引
    },

    // 结束拖拽
    onEnd: function (/**Event*/evt) {
        var itemEl = evt.item;  // dragged HTMLElement
        evt.to;    // target list
        evt.from;  // previous list
        evt.oldIndex;  // 元素在旧父元素中的旧索引
        evt.newIndex;  // 元素在新父元素中的新索引
        evt.clone // the clone element
        evt.pullMode;  // 当项目在另一个可排序:“克隆”如果克隆，“真”如果移动
    },

    // 元素从一个列表拖拽到另一个列表
    onAdd: function (/**Event*/evt) {
        // 与onEnd相同的属性
    },

    // 列表内元素顺序更新的时候触发
    onUpdate: function (/**Event*/evt) {
        // 与onEnd相同的属性
    },

    // 列表的任何更改都会触发
    onSort: function (/**Event*/evt) {
        // 与onEnd相同的属性
    },

    // 元素从列表中移除进入另一个列表
    onRemove: function (/**Event*/evt) {
        // 与onEnd相同的属性
    },

    // 试图拖拽一个filtered的元素
    onFilter: function (/**Event*/evt) {
        var itemEl = evt.item;  // HTMLElement接收' mousedown|tapstart '事件。
    },

    // 拖拽移动的时候
    onMove: function (/**Event*/evt, /**Event*/originalEvent) {
        // Example: https://jsbin.com/nawahef/edit?js,output
        evt.dragged; // dragged HTMLElement
        evt.draggedRect; // DOMRect {left, top, right, bottom}
        evt.related; // HTMLElement on which have guided
        evt.relatedRect; // DOMRect
        evt.willInsertAfter; // 布尔值，如果Sortable将默认在目标后插入拖动元素，则为真
        originalEvent.clientY; // 鼠标位置
        // return false; — for cancel
        // return -1; — insert before target
        // return 1; — insert after target
    },

    // 在创建元素的克隆时调用
    onClone: function (/**Event*/evt) {
        var origEl = evt.item;
        var cloneEl = evt.clone;
    },

    // 当拖动元素改变位置时调用
    onChange: function(/**Event*/evt) {
        evt.newIndex // 使用此事件的最可能原因是获取拖动元素的当前索引
        // 与onEnd相同的属性
    }
});