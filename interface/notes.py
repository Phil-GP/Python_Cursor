import tkinter as tk
from tkinter import filedialog, messagebox

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("600x400")

        self._modified = False

        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        self.text_area.bind("<<Modified>>", self._on_modified)

        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.criar_menu()

    def criar_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_arquivo)
        filemenu.add_command(label="Salvar", command=self.salvar_arquivo)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=self.on_exit)
        menubar.add_cascade(label="Arquivo", menu=filemenu)
        self.config(menu=menubar)

    def _on_modified(self, event=None):
        # Marcar que houve alteração e limpar o flag interno do Tkinter
        self._modified = True
        self.text_area.edit_modified(False)

    def _reset_modified(self):
        self._modified = False
        self.text_area.edit_modified(False)

    def on_exit(self):
        if not self._modified:
            self.destroy()
            return

        resposta = messagebox.askyesnocancel(
            "Sair",
            "O documento foi modificado. Deseja salvar antes de sair?",
        )
        if resposta is None:
            # Cancelar
            return
        if resposta:
            # Sim: salvar e depois sair se conseguiu
            self.salvar_arquivo()
            if not self._modified:
                self.destroy()
        else:
            # Não: sair sem salvar
            self.destroy()

    def abrir_arquivo(self):
        caminho = filedialog.askopenfilename(
            title="Abrir arquivo de texto",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
        )
        if not caminho:
            return

        try:
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, conteudo)
            self._reset_modified()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo:\n{e}")

    def salvar_arquivo(self):
        caminho = filedialog.asksaveasfilename(
            title="Salvar como",
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
        )
        if not caminho:
            return

        conteudo = self.text_area.get("1.0", tk.END)
        try:
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(conteudo.rstrip("\n"))
            messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")
            self._reset_modified()
        except OSError as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")


if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()