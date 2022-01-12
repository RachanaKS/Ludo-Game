# For same position, previous coin deleted and set to the room
def coord_overlap(self, counter_coin, color_coin, path_to_traverse_before_overlap):
    if color_coin != "red":
        for take_coin_number in range(len(self.red_coord_store)):
            if self.red_coord_store[take_coin_number] == counter_coin:
                if path_to_traverse_before_overlap == 6:
                    self.six_with_overlap = 1
                else:
                    self.time_for -= 1

                self.make_canvas.delete(self.made_red_coin[take_coin_number])
                self.red_number_label[take_coin_number].place_forget()
                self.red_coin_position[take_coin_number] = -1
                self.red_coord_store[take_coin_number] = -1
                if self.robo_prem == 1:
                    self.robo_store.remove(take_coin_number + 1)
                    if self.red_coin_position.count(-1) >= 1:
                        self.count_robo_stage_from_start = 2

                if take_coin_number == 0:
                    remade_coin = self.make_canvas.create_oval(100 + 40, 15 + 40, 100 + 40 + 40, 15 + 40 + 40, width=3,
                                                               fill="red", outline="black")
                    self.red_number_label[take_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 5)
                elif take_coin_number == 1:
                    remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40, 100 + 40 + 60 + 60 + 40,
                                                               15 + 40 + 40, width=3, fill="red", outline="black")
                    self.red_number_label[take_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 5)
                elif take_coin_number == 2:
                    remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100,
                                                               100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100, width=3,
                                                               fill="red", outline="black")
                    self.red_number_label[take_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 100 + 5)
                else:
                    remade_coin = self.make_canvas.create_oval(100 + 40, 15 + 40 + 100, 100 + 40 + 40,
                                                               15 + 40 + 40 + 100, width=3, fill="red", outline="black")
                    self.red_number_label[take_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)

                self.made_red_coin[take_coin_number] = remade_coin

    if color_coin != "green":
        for take_coin_number in range(len(self.green_coord_store)):
            if self.green_coord_store[take_coin_number] == counter_coin:
                if path_to_traverse_before_overlap == 6:
                    self.six_with_overlap = 1
                else:
                    self.time_for -= 1

                self.make_canvas.delete(self.made_green_coin[take_coin_number])
                self.green_number_label[take_coin_number].place_forget()
                self.green_coin_position[take_coin_number] = -1
                self.green_coord_store[take_coin_number] = -1

                if take_coin_number == 0:
                    remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 15 + 40, 340 + (40 * 3) + 40 + 40,
                                                               15 + 40 + 40, width=3, fill="#00FF00", outline="black")
                    self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
                elif take_coin_number == 1:
                    remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40,
                                                               340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40,
                                                               width=3, fill="#00FF00", outline="black")
                    self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 5)
                elif take_coin_number == 2:
                    remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100,
                                                               340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                               15 + 40 + 40 + 100, width=3, fill="#00FF00",
                                                               outline="black")
                    self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                    y=15 + 40 + 100 + 5)
                else:
                    remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 15 + 40 + 100,
                                                               340 + (40 * 3) + 40 + 40, 15 + 40 + 40 + 100, width=3,
                                                               fill="#00FF00", outline="black")
                    self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 100 + 5)

                self.made_green_coin[take_coin_number] = remade_coin

    if color_coin != "yellow":
        for take_coin_number in range(len(self.yellow_coord_store)):
            if self.yellow_coord_store[take_coin_number] == counter_coin:
                if path_to_traverse_before_overlap == 6:
                    self.six_with_overlap = 1
                else:
                    self.time_for -= 1

                self.make_canvas.delete(self.made_yellow_coin[take_coin_number])
                self.yellow_number_label[take_coin_number].place_forget()
                self.yellow_coin_position[take_coin_number] = -1
                self.yellow_coord_store[take_coin_number] = -1

                if take_coin_number == 0:
                    remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340 + 80 + 15,
                                                               340 + (40 * 3) + 40 + 40, 340 + 80 + 40 + 15, width=3,
                                                               fill="yellow", outline="black")
                    self.yellow_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 10,
                                                                     y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                elif take_coin_number == 1:
                    remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                                               340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                               340 + 80 + 40 + 15, width=3, fill="yellow",
                                                               outline="black")
                    self.yellow_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                     y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                elif take_coin_number == 2:
                    remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20,
                                                               340 + 80 + 60 + 40 + 15,
                                                               340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                               340 + 80 + 60 + 40 + 40 + 15, width=3, fill="yellow",
                                                               outline="black")
                    self.yellow_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                     y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
                else:
                    remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340 + 80 + 60 + 40 + 15,
                                                               340 + (40 * 3) + 40 + 40, 340 + 80 + 60 + 40 + 40 + 15,
                                                               width=3, fill="yellow", outline="black")
                    self.yellow_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 10,
                                                                     y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)

                self.made_yellow_coin[take_coin_number] = remade_coin

    if color_coin != "sky_blue":
        for take_coin_number in range(len(self.sky_blue_coord_store)):
            if self.sky_blue_coord_store[take_coin_number] == counter_coin:
                if path_to_traverse_before_overlap == 6:
                    self.six_with_overlap = 1
                else:
                    self.time_for -= 1

                self.make_canvas.delete(self.made_sky_blue_coin[take_coin_number])
                self.sky_blue_number_label[take_coin_number].place_forget()
                self.sky_blue_coin_position[take_coin_number] = -1
                self.sky_blue_coord_store[take_coin_number] = -1

                if take_coin_number == 0:
                    remade_coin = self.make_canvas.create_oval(100 + 40, 340 + 80 + 15, 100 + 40 + 40,
                                                               340 + 80 + 40 + 15, width=3, fill="#04d9ff",
                                                               outline="black")
                    self.sky_blue_number_label[take_coin_number].place(x=100 + 40 + 10,
                                                                       y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                elif take_coin_number == 1:
                    remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                                               100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 40 + 15,
                                                               width=3, fill="#04d9ff", outline="black")
                    self.sky_blue_number_label[take_coin_number].place(x=100 + 40 + 60 + 60 + 10,
                                                                       y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                elif take_coin_number == 2:
                    remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15,
                                                               100 + 40 + 60 + 40 + 40 + 20,
                                                               340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#04d9ff",
                                                               outline="black")
                    self.sky_blue_number_label[take_coin_number].place(x=100 + 40 + 60 + 60 + 10,
                                                                       y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
                else:
                    remade_coin = self.make_canvas.create_oval(100 + 40, 340 + 80 + 60 + 40 + 15, 100 + 40 + 40,
                                                               340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#04d9ff",
                                                               outline="black")
                    self.sky_blue_number_label[take_coin_number].place(x=100 + 40 + 10,
                                                                       y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)

                self.made_sky_blue_coin[take_coin_number] = remade_coin
