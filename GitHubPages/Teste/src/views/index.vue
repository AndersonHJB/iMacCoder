<template>
  <div>
    <div class="header full-width">
      <div class="flex-1-1-auto">
        <!-- <img src="../assets/logo.svg" alt="" /> -->
        <!-- 后期更换logo就把下面一行注释掉,上面一行src换成你的logo,并取消注释 -->
        <div class="logo">AI悦创在线编程|社区</div>
      </div>
      <div class="flex-none">
        <div class="searchbox_search-box">
          <img
            src="../assets/edit.svg"
            alt=""
            style="transform: scale(0.7, 0.7)"
          />
          <input
            type="text"
            placeholder="这是我的作品名称"
            value=""
            v-model="file_name"
          />
        </div>
      </div>
      <div class="header_py-btn">
        <a class="header_py-btn__hiNW1 logo" href="https://www.bornforthis.cn/"
          >Python编程指南</a
        >
        <div class="header_btn_">
          <a class="release" href="https://www.aiycoj.cn/">
            <div
              class="button_header-button__xiNgO"
              style="width: 96px; padding: 0px"
            >
              发布
            </div></a
          >
        </div>
        <div class="header_btn_">
          <div
            class="button_header-button__xiNgO"
            style="width: 96px; padding: 0px"
            @click="saveFile"
          >
            保存
          </div>
        </div>
        <div class="header_right"></div>
      </div>
    </div>
    <div class="main">
      <div
        class="codeandconsole"
        :class="{ display_none: is_full_screen }"
        id="codeandconsole"
      >
        <div class="code" id="code"></div>
        <div class="console" id="console">
          <div ref="output" class="output">
            <div class="component_repl-ct" id="output">
              <span
                v-for="(item, index) in output"
                :key="index"
                v-html="item"
              ></span>
              <input
                v-model="input_msg"
                class="input"
                readonly="true"
                id="input"
              />
            </div>
          </div>
          <div class="console_btn">
            <div
              class="console_btn_container clear_console"
              @click="canvas_hide_handler"
            >
              <div>{{ canvas_hide ? "显示" : "隐藏" }}画布</div>
            </div>
            <div
              class="console_btn_container clear_console"
              :class="{ display_none: is_processing }"
              @click="clearConsole"
            >
              <div>清除终端</div>
            </div>
            <div class="console_btn_container" @click="run()">
              <div>{{ is_processing ? "停止" : "开始" }}</div>
            </div>
          </div>
        </div>
      </div>
      <div
        ref="canvas"
        class="canvas"
        :style="{ display: canvas_hide ? 'none' : '' }"
      >
        <div class="src_ct">
          <div
            class="src_tutle"
            id="turtleCanvas"
            :class="{ display_none: canvas_show }"
            :style="{ right: right_px, bottom: bottom_px }"
          ></div>
          <div class="wangge">
            <div :class="is_grid ? '' : 'wanggexian'" id="wanggexian"></div>
          </div>
        </div>
        <div class="btn_container">
          <div class="btn_canvas">
            <img src="../assets/mesh.svg" @click="toggle_grid()" />
          </div>
          <div class="btn_canvas">
            <img
              :src="
                is_full_screen
                  ? '../assets/exitfullscreen.svg'
                  : '../assets/enterfullscreen.svg'
              "
              @click="toggle_full_screen()"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "skulpt/dist/skulpt.min.js";
import "skulpt/dist/skulpt-stdlib.js";
import "ace-builds/src-min-noconflict/ace.js";
import "ace-builds/src-min-noconflict/ext-language_tools.js";
import "ace-builds/src-min-noconflict/mode-python.js";
import "ace-builds/src-min-noconflict/theme-monokai.js";
export default {
  mounted() {
    window.vm = this;
    //  窗口大小变化时，计算canvas偏移量
    this.canvansHeight = this.$refs.canvas.clientHeight + "px";
    this.canvansWidth = this.$refs.canvas.clientWidth + "px";
    window.onresize = () => {
      this.bottom_px =
        (this.canvansHeight.slice(0, -2) - this.$refs.canvas.clientHeight) / 2 +
        "px";
      this.right_px =
        (this.canvansWidth.slice(0, -2) - this.$refs.canvas.clientWidth) / 2 +
        "px";
    };
    // 监听画布全屏时，计算canvas偏移量
    var elementResizeDetectorMaker = require("element-resize-detector");
    var erd = elementResizeDetectorMaker();
    erd.listenTo(this.$refs.canvas, function (element) {
      var event = document.createEvent("HTMLEvents");
      event.initEvent("resize", true, true);
      window.dispatchEvent(event);
    });
    // 初始化ace编辑器
    ace.require("ace/ext/language_tools");
    var editor = ace.edit("code");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.setOptions({
      enableBasicAutocompletion: true, //
      enableLiveAutocompletion: true, // 补全
      fontSize: "18px",
    });
  },
  data() {
    return {
      canvas_show: false, //画布展示，仅作品的清除
      is_processing: false, //是否显示清除输出按钮
      is_grid: false, //网格线显示
      is_full_screen: false, //画布全屏
      output: ["欢迎来到悦创小图灵的世界! Happy Coding :)\n"], //控制台输出
      StopExecution: false, //终止运行标识
      canvansHeight: "0px",
      canvansWidth: "0px",
      right_px: 0, //偏移量
      bottom_px: 0, //偏移量
      input_msg: "",
      file_name: "",
      canvas_hide: false, //画布隐藏,代码编辑全屏
    };
  },
  methods: {
    toggle_grid() {
      //展示/清除网格线
      this.is_grid = !this.is_grid;
    },
    toggle_full_screen() {
      //全屏/退出全屏
      this.is_full_screen = !this.is_full_screen;
    },

    builtinRead(x) {
      //Sk配置
      if (
        Sk.builtinFiles === undefined ||
        Sk.builtinFiles["files"][x] === undefined
      )
        throw "File not found: '" + x + "'";
      return Sk.builtinFiles["files"][x];
    },
    outf(text) {
      //Sk输出处理
      this.output.push(text);
      var that = this;
      //自动滚动至底部
      this.$nextTick(() => {
        that.$refs.output.scrollTop = that.$refs.output.scrollHeight;
      });
      console.log("outputt");
    },
    inputfunc() {
      var that = this;
      console.log("input");
      var input = document.getElementById("input");
      input.removeAttribute("readonly");
      input.focus();
      return new Promise(function (resolve, reject) {
        input.addEventListener("keyup", function (e) {
          // that.input_msg = ;
          var result = input.value;
          console.log("result" + result);
          if (e.key == "Enter") {
            console.log("enter");
            var new_input = document.createElement("input");
            new_input.setAttribute("id", "input");
            new_input.setAttribute("readonly", "readonly");
            new_input.setAttribute(
              "style",
              "color: white;width: 100%;display:inline;position: absolute;background: transparent;outline: none;border: none;"
            );
            input.parentNode.replaceChild(new_input, input);
            // // resolve the promise with the value of the input field
            that.input_msg = "";
            console.log(that.StopExecution);
            console.log("result" + result);
            if (that.StopExecution) {
              reject("input");
            } else {
              // remove keyup handler from #output
              console.log(result);
              that.outf(result + "\n");
              resolve(result);
            }
          }
        });
      });
    },
    run_code() {
      var that = this;
      var code = ace.edit("code").getValue();
      Sk.configure({
        output: this.outf,
        inputfun: this.inputfunc,
        read: this.builtinRead,
        killableWhile: true,
        inputTakesPrompt: true,
      });
      (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = "turtleCanvas";
      Sk.TurtleGraphics.width = this.$refs.canvas.clientWidth;
      Sk.TurtleGraphics.height = this.$refs.canvas.clientHeight;
      Sk.misceval
        .asyncToPromise(
          () => Sk.importMainWithBody("<stdin>", false, code, true),
          {
            //监听停止运行
            "*": () => {
              if (that.StopExecution) {
                that.StopExecution = false;
                throw "<font color='red'>\n程序中止运行\n</font>";
              }
            },
          }
        )
        .then(
          function (mod) {
            if (!that.StopExecution) {
              that.outf("<font color='#36ff00'>\n程序运行结束～\n</font>");
            }
            that.is_processing = false;
          },
          function (err) {
            if (JSON.parse(JSON.stringify(err)).nativeError == "input") {
              throw "<font color='red'>\n程序中止运行\n</font>";
            } else {
              throw "<font color='red'>" + err.toString() + "</font>";
            }
          }
        )
        .catch((err) => {
          this.outf("<font color='red'>" + err.toString() + "</font>");
          console.log(err);
        })
        .finally(() => {
          console.log("finally");
          that.is_processing = false;
        });
    },
    run() {
      if (this.is_processing) {
        //停止
        this.is_processing = false;
        this.StopExecution = true;
        var event = new KeyboardEvent("keyup", {
          key: "Enter",
          keyCode: 13,
        });
        document.getElementById("input").dispatchEvent(event);
        console.log("我的任务完成了");
      } else {
        //运行
        this.canvas_show = false;
        this.is_processing = true;
        this.StopExecution = false;
        this.run_code();
      }
    },
    clearConsole() {
      //清空控制台
      this.output = [];
      //清除画布
      this.canvas_show = true;
    },
    saveFile() {
      var code = ace.edit("code").getValue();
      //定义文件内容，类型必须为Blob 否则createObjectURL会报错
      let content = new Blob([code], { type: "text/plain" });
      //生成url对象
      let urlObject = window.URL || window.webkitURL || window;
      let url = urlObject.createObjectURL(content);
      //生成<a></a>DOM元素
      let el = document.createElement("a");
      //链接赋值
      el.href = url;
      el.download = this.file_name + ".py";
      //必须点击否则不会下载
      el.click();
      //移除链接释放资源
      urlObject.revokeObjectURL(url);
    },
    canvas_hide_handler() {
      this.canvas_hide = !this.canvas_hide;
    },
  },
};
</script>

<style  scoped>
* {
  margin: 0;
  padding: 0;
}

.header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 60px;
  padding-left: 20px;
  background-color: #3c70ff;
  box-sizing: border-box;
}

.header > div {
  display: flex;
}

.full-width {
  min-width: 1200px;
  width: 100%;
  box-sizing: border-box;
}

.flex-1-1-auto {
  flex: 1 1 auto;
}

.flex-none {
  flex: none;
}

.logo {
  color: white;
  font-size: 20px;
  line-height: 60px;
  height: 60px;
  text-decoration: none;
}

.searchbox_search-box {
  width: 394px;
  height: 40px;
  background: rgba(245, 247, 250, 0.3);
  border-radius: 12px;
  padding: 0 12px 0 7px;
  display: flex;
}

.header .header_py-btn {
  flex: 1 0 auto;
  justify-content: flex-end;
  align-items: center;
}

.header .header_py-btn .header_py-btn__hiNW1 {
  margin-right: 44px;
  cursor: pointer;
}

.header_btn_ {
  margin-right: 12px;
}

.button_header-button__xiNgO {
  background: #fff;
  border-radius: 27px;
  padding: 0 32px;
  line-height: 36px;
  font-size: 16px;
  font-weight: 400;
  color: #3c70ff;
  text-align: center;
  cursor: pointer;
}

.searchbox_search-box > input {
  display: block;
  color: #fff;
  outline: none;
  border: 0;
  background: transparent;
  line-height: 40px;
  font-size: 16px;
  width: 100%;
}

.header_right {
  margin-right: 22px;
}

.main {
  display: flex;
  margin: 25px 20px;
  justify-content: space-between;
  align-items: flex-start;
  min-width: 1150px;
  min-height: 576px;
  height: calc(100vh - 60px - 50px);
  box-sizing: border-box;
}

.codeandconsole {
  display: flex;
  height: 100%;
  flex: 1 1 55%;
  margin-right: 19px;
  flex-direction: column;
  justify-content: space-between;
  align-items: stretch;
  box-sizing: border-box;
}

.canvas {
  position: relative;
  height: 100%;
  flex: 1 1 45%;
  box-sizing: border-box;
  overflow: hidden;
  align-items: center;
}

.code {
  width: 100%;
  flex: 1 1;
  margin-bottom: 18px;
  border-radius: 16px;
  border: 1px solid #ededef;
  /* overflow: scroll */
}

.console {
  display: flex;
  width: 100%;
  flex: 0 0 270px;
  border-radius: 16px;
  border: 1px solid #ededef;
  background: #1f242e;
  overflow: hidden;
  flex-direction: column;
  justify-content: space-between;
  align-items: stretch;
  box-sizing: border-box;
  font-size: 14px;
}

.src_ct .src_meshCt__2huzy {
  position: absolute;
  pointer-events: none;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: #fff;
  border: 1px solid #ededef;
  box-sizing: border-box;
  border-radius: 16px;
  padding: 16px 26px;
}

.src_ct .src_tutle {
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: 1;
  outline: none;
}

@media (max-width: 736px) {
  .src_ct .src_tutle {
    transform: scale(0.3);
  }
}

.wangge {
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -2;
  outline: none;
  position: absolute;
  pointer-events: none;
  left: 0;
  top: 0;
  background: #fff;
  border: 1px solid #ededef;
  box-sizing: border-box;
  border-radius: 16px;
}

.wanggexian {
  background-color: #ffffff;
  /*背景色*/
  background-image: linear-gradient(
      90deg,
      rgba(141, 141, 141, 0.15) 5%,
      rgba(0, 0, 0, 0) 5%
    ),
    linear-gradient(0deg, rgba(141, 141, 141, 0.15) 5%, rgba(0, 0, 0, 0) 5%);
  /*rgba(0, 0, 0, 0)，transparent全透明黑*/
  background-size: 20px 20px;
  /*调节格子宽 高*/
  background-clip: content-box;
  background-origin: border-box;
  height: calc(100% - 26px);
  padding: 16px 26px;
}

.btn_container {
  display: flex;
  position: absolute;
  top: 6px;
  right: 16px;
  z-index: 999;
}

.btn_canvas {
  cursor: pointer;
  width: 36px;
  height: 36px;
  border-radius: 8px;
  margin-right: 12px;
}

.display_none {
  display: none;
}

.output {
  flex: 1 1 65%;
  overflow-y: auto;
  width: 100%;
  color: #fff;
  padding-left: 20px;
  padding-bottom: 10px;
  box-sizing: border-box;
  /* overflow: scroll; */
}

.component_repl-ct {
  width: 100%;
  white-space: pre-wrap;
  position: relative;
  display: inline;
}

.console_btn {
  display: flex;
  width: 100%;
  flex: 1 1 35%;
  overflow: hidden;
  background: hsla(0, 0%, 100%, 0.06);
  justify-content: flex-end;
  align-items: center;
  box-sizing: border-box;
  color: white;
}

.console_btn_container {
  font-weight: 600;
  font-size: 20px;
  height: 48px;
  line-height: 48px;
  border-radius: 34px;
  background: linear-gradient(254.9deg, #3098ff 23.81%, #3c70ff 76.38%);
  padding: 0 32px 0 28px;
  margin: 0 10px;
  cursor: pointer;
}

.clear_console {
  background: hsla(0, 0%, 100%, 0.25);
  border: 1px solid hsla(0, 0%, 100%, 0.25);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
}
.input {
  color: white;
  width: 100%;
  background: transparent;
  outline: none;
  border: none;
  display: inline;
  position: absolute;
}
input::placeholder {
  color: white;
}

/* .turtleCanvas {
  position: relative;
} */
.release {
  color: inherit;
  text-decoration: none;
}
</style>

