mouse_active = False  # Canvas内にマウスがある間だけ True

def start_button_on_click(event):
    """スタートボタンがクリックされたときの処理"""
    # スタートボタンの無効化
    document.getElementById("start_button").disabled = True
    init_game() # ゲーム初期化
    game_loop() # ゲームループ開始

def start_button_on_click(event):
    """スタートボタンがクリックされたときの処理"""
    document.getElementById("start_button").disabled = True
    init_game()
    game_loop()

def set_player_x_from_mouse(client_x):
    """マウスのX座標(clientX)からバー位置(px)を計算して反映（水平のみ）"""
    if game["game_over"]:
        return

    rect = canvas.getBoundingClientRect()
    x = client_x - rect.left  # Canvas内のX座標に変換

    # バー中心がマウス位置に来るようにする
    px = x - (PLAYER_W / 2)

    # 画面外に出ないようにクランプ
    if px < 0:
        px = 0
    max_px = canvas.width - PLAYER_W
    if px > max_px:
        px = max_px

    game["px"] = px
    draw_screen()

def on_mouse_enter(event):
    global mouse_active
    mouse_active = True

def on_mouse_leave(event):
    global mouse_active
    mouse_active = False

def on_mouse_move(event):
    # 「ある領域（=canvas）」に入っている間だけ動かす
    if not mouse_active:
        return
    set_player_x_from_mouse(event.clientX)

# --- マウスイベント登録（Canvasを“領域”にする） ---
canvas.addEventListener("mouseenter", on_mouse_enter)
canvas.addEventListener("mouseleave", on_mouse_leave)
canvas.addEventListener("mousemove", on_mouse_move)

def player_move(dx):
    """プレイヤーのバーを移動する"""
    if game["game_over"]:
        return  # ゲームオーバー時は移動しない
    px = game["px"] + dx  # 新しいバーの位置
    # バーが画面外に出ないように制限
    if 0 <= px <= (canvas.width - PLAYER_W):
        game["px"] = px
        draw_screen()

def key_down(event):
    """キーが押されたときの処理"""
    if event.key == "ArrowRight":
       player_move(PLAYER_MOVE)  # 右に移動
    elif event.key == "ArrowLeft":
        player_move(-1 * PLAYER_MOVE)  # 左に移動

# キー押下イベントリスナーの登録
document.addEventListener("keydown", key_down)
