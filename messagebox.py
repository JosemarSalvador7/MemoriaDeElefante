"""
Módulo CTkMessageBox - Implementação CustomTkinter para messagebox
Autor: [Seu Nome]
Versão: 1.0
"""

import customtkinter as ctk
from typing import Optional, Literal


class CTkMessageBox(ctk.CTkToplevel):
    """Janela de diálogo personalizada com CustomTkinter"""
    
    def __init__(
        self,
        title: str = "Message",
        message: str = "",
        icon: Optional[str] = None,
        button_names: tuple = ("OK",),
        default_button: str = None,
        width: int = 400,
        height: int = 200,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        # Configurações da janela
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)
        
        # Centralizar na tela
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"+{x}+{y}")
        
        # Variável para armazenar resultado
        self.result = None
        
        # Criar widgets
        self._create_widgets(message, icon, button_names, default_button)
        
        # Configurar comportamento do fechamento
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        
        # Tornar modal
        self.grab_set()
        self.focus()
        
    def _create_widgets(self, message: str, icon: Optional[str], 
                       button_names: tuple, default_button: str):
        """Cria os widgets da janela de diálogo"""
        
        # Frame principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        main_frame = ctk.CTkFrame(self, corner_radius=10)
        main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        
        # Frame de conteúdo
        content_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        content_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        content_frame.grid_columnconfigure(1, weight=1)
        
        # Ícone (se fornecido)
        if icon:
            icon_label = ctk.CTkLabel(
                content_frame,
                text=icon,
                font=("Arial", 32),
                width=50,
                height=50
            )
            icon_label.grid(row=0, column=0, padx=(0, 15), sticky="nw")
        
        # Mensagem
        message_label = ctk.CTkLabel(
            content_frame,
            text=message,
            font=("Arial", 14),
            wraplength=300,
            justify="left"
        )
        message_label.grid(
            row=0, 
            column=1 if icon else 0, 
            columnspan=2 if not icon else 1,
            sticky="nsew",
            padx=(0, 10) if icon else 0
        )
        
        # Frame dos botões
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="e")
        
        # Botões
        self.buttons = {}
        for i, btn_name in enumerate(button_names):
            btn = ctk.CTkButton(
                button_frame,
                text=btn_name,
                width=80,
                height=32,
                command=lambda name=btn_name: self._button_click(name)
            )
            btn.grid(row=0, column=i, padx=(5, 0))
            self.buttons[btn_name] = btn
            
            # Botão padrão
            if btn_name == default_button:
                btn.focus_set()
    
    def _button_click(self, button_name: str):
        """Lida com o clique nos botões"""
        self.result = button_name
        self.grab_release()
        self.destroy()
    
    def _on_close(self):
        """Lida com o fechamento da janela"""
        self.result = None
        self.grab_release()
        self.destroy()
    
    def show(self) -> Optional[str]:
        """Mostra a janela e retorna o resultado"""
        self.wait_window()
        return self.result


# Funções principais do módulo
def showinfo(title: str = "Information", message: str = "", **kwargs) -> None:
    """Mostra uma mensagem informativa"""
    dialog = CTkMessageBox(
        title=title,
        message=message,
        icon="ℹ️",
        button_names=("OK",),
        default_button="OK",
        **kwargs
    )
    dialog.show()


def showwarning(title: str = "Warning", message: str = "", **kwargs) -> None:
    """Mostra uma mensagem de aviso"""
    dialog = CTkMessageBox(
        title=title,
        message=message,
        icon="⚠️",
        button_names=("OK",),
        default_button="OK",
        **kwargs
    )
    dialog.show()


def showerror(title: str = "Error", message: str = "", **kwargs) -> None:
    """Mostra uma mensagem de erro"""
    dialog = CTkMessageBox(
        title=title,
        message=message,
        icon="❌",
        button_names=("OK",),
        default_button="OK",
        **kwargs
    )
    dialog.show()


def askquestion(title: str = "Question", message: str = "", **kwargs) -> Literal["Yes", "No"]:
    """Pergunta com opções Sim/Não - retorna 'Yes' ou 'No'"""
    dialog = CTkMessageBox(
        title=title,
        message=message,
        icon="?",
        button_names=("Yes", "No"),
        default_button="Yes",
        **kwargs
    )
    result = dialog.show()
    return result if result else "No"


def askokcancel(title: str = "Confirm", message: str = "", **kwargs) -> bool:
    """Pergunta com opções OK/Cancelar - retorna True para OK, False para Cancelar"""
    dialog = CTkMessageBox(
        title=title,
        message=message,
        icon="?",
        button_names=("OK", "Cancel"),
        default_button="OK",
        **kwargs
    )
    result = dialog.show()
    return result == "OK"


def askyesno(title: str = "Confirm", message: str = "", **kwargs) -> bool:
    """Pergunta com opções Sim/Não - retorna True para Sim, False para Não"""
    dialog = CTkMessageBox(
        title=title,
        message=message,
        icon="?",
        button_names=("Yes", "No"),
        default_button="Yes",
        **kwargs
    )
    result = dialog.show()
    return result == "Yes"


def askyesnocancel(title: str = "Confirm", message: str = "", **kwargs) -> Optional[bool]:
    """Pergunta com opções Sim/Não/Cancelar - retorna True/False/None"""
    dialog = CTkMessageBox(
        title=title,
        message=message,
        icon="?",
        button_names=("Yes", "No", "Cancel"),
        default_button="Yes",
        **kwargs
    )
    result = dialog.show()
    
    if result == "Yes":
        return True
    elif result == "No":
        return False
    else:
        return None


def askretrycancel(title: str = "Retry", message: str = "", **kwargs) -> bool:
    """Pergunta com opções Repetir/Cancelar - retorna True para Repetir"""
    dialog = CTkMessageBox(
        title=title,
        message=message,
        icon="🔄",
        button_names=("Retry", "Cancel"),
        default_button="Retry",
        **kwargs
    )
    result = dialog.show()
    return result == "Retry"


# Função para demonstração/teste
def demo():
    """Demonstração de todas as funções do módulo"""
    import time
    
    app = ctk.CTk()
    app.title("CTkMessageBox Demo")
    app.geometry("400x500")
    
    def test_showinfo():
        showinfo("Information", "This is an information message!")
    
    def test_showwarning():
        showwarning("Warning", "This is a warning message!")
    
    def test_showerror():
        showerror("Error", "This is an error message!")
    
    def test_askquestion():
        result = askquestion("Question", "Do you like CTkMessageBox?")
        print(f"AskQuestion result: {result}")
    
    def test_askokcancel():
        result = askokcancel("Confirmation", "Do you want to proceed?")
        print(f"AskOkCancel result: {result}")
    
    def test_askyesno():
        result = askyesno("Confirmation", "Are you sure?")
        print(f"AskYesNo result: {result}")
    
    def test_askyesnocancel():
        result = askyesnocancel("Confirmation", "Save changes?")
        print(f"AskYesNoCancel result: {result}")
    
    def test_askretrycancel():
        result = askretrycancel("Retry", "Operation failed. Retry?")
        print(f"AskRetryCancel result: {result}")
    
    # Botões de teste
    buttons = [
        ("Show Info", test_showinfo),
        ("Show Warning", test_showwarning),
        ("Show Error", test_showerror),
        ("Ask Question", test_askquestion),
        ("Ask OK/Cancel", test_askokcancel),
        ("Ask Yes/No", test_askyesno),
        ("Ask Yes/No/Cancel", test_askyesnocancel),
        ("Ask Retry/Cancel", test_askretrycancel),
    ]
    
    for i, (text, command) in enumerate(buttons):
        btn = ctk.CTkButton(
            app,
            text=text,
            command=command,
            height=40,
            font=("Arial", 14)
        )
        btn.pack(pady=10, padx=20, fill="x")
    
    app.mainloop()


if __name__ == "__main__":
    demo()