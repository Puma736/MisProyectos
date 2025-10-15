unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.ExtCtrls, Vcl.Imaging.pngimage,
  Vcl.Imaging.jpeg, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Image1: TImage;
    Image2: TImage;
    ImageObst1: TImage;
    ImageObst2: TImage;
    ImgHelicop: TImage;
    imgHelice: TImage;
    Timer1: TTimer;
    Image7: TImage;
    Panel1: TPanel;
    Button1: TButton;
    Button2: TButton;
    Label1: TLabel;
    Label2: TLabel;
    procedure FormMouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure FormMouseUp(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure Timer1Timer(Sender: TObject);
    procedure FormResize(Sender: TObject);
    procedure iniciarJuego;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
    function colision(obj1,obj2:Timage):boolean;
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  rotarhelice:integer = 1;
  mousepresionado  :boolean = false;

  distancia : integer = 0;
  velocidadObstaculo : integer = 8;


implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
begin
  panel1.Visible:= false;
  iniciarJuego;

end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  application.Terminate;
end;

function TForm1.colision(obj1, obj2: Timage): boolean;
begin
  result:= obj1.BoundsRect.IntersectsWith(obj2.BoundsRect);
end;

procedure TForm1.FormMouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
   if button = mbleft then
   begin
      ImgHelicop.Top:= ImgHelicop.Top - 20;
      mousePresionado:= True;
   end;
end;

procedure TForm1.FormMouseUp(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
  mousePresionado:= false;
end;

procedure TForm1.FormResize(Sender: TObject);
begin
  Panel1.Left := (ClientWidth div 2) - (Panel1.Width div 2);
  Panel1.Top  := (ClientHeight div 2) - (Panel1.Height div 2);
end;

procedure TForm1.iniciarJuego;
begin
  distancia := 0;
  velocidadObstaculo := 5;
  imgHelicop.Left := 100;
  imgHelicop.Top := 200;
  mousePresionado := False;
  //Frame := 1;

  // Volver a colocar obstáculos
  ImageObst1.Left := Width;
  ImageObst2.Left := Width + 300;
  Timer1.Enabled := True;

end;

procedure TForm1.Timer1Timer(Sender: TObject);
begin
   case rotarHelice of
     1:imgHelice.Picture.LoadFromFile('elise1_1.png');
     2:imgHelice.Picture.LoadFromFile('elise2.png');
     3:imgHelice.Picture.LoadFromFile('elise3.png');
     4:imgHelice.Picture.LoadFromFile('elise4.png');
   end;


   rotarHelice:= rotarHelice + 1;
   if rotarHelice > 4 then
      rotarHelice:=1;

   if MousePresionado then
   begin
    imgHelicop.Top := imgHelicop.Top - 2;  // sube
   end
   else
   begin
    imgHelicop.Top := imgHelicop.Top + 3;  // baja
   end;

   imgHelice.Left := imgHelicop.Left + 40; // derecha
   imgHelice.Top := imgHelicop.Top - 0;    // arriba



  // Mover obstáculos
   ImageObst1.Left := ImageObst1.Left - velocidadObstaculo;
   ImageObst2.Left := ImageObst2.Left - velocidadObstaculo;

   if ImageObst1.Left + ImageObst1.Width < 0 then
   begin
     ImageObst1.Left := Width;
     ImageObst1.Top := 50 + Random(ClientHeight - 150);
   end;

   if ImageObst2.Left + ImageObst2.Width < 0 then
   begin
     ImageObst2.Left := ImageObst1.Left + 300;
   // ImageObst2.Top := 50 + Random(ClientHeight - 150);
   end;

  //colisión
   if Colision(ImageObst1,imgHelicop) or Colision(ImageObst2,imgHelicop)or
     Colision(ImageObst1, imgHelice) or Colision(ImageObst2, imgHelice)or
     Colision(Image1, imgHelicop) or Colision(Image1, imgHelice) or
     Colision(Image2, imgHelicop) or Colision(Image2, imgHelice) then
   begin
    Timer1.Enabled := False;
    ShowMessage('¡Colision fin del Juego! Game Over.');
    Panel1.Visible := True;
   end;

  // Act distancia
   distancia := distancia + 1;
   Label1.Caption := 'Distancia: ' + IntToStr(distancia) + ' m';

  // Aumt veloc cad 100 mt
   if distancia mod 100 = 0 then
   begin
   velocidadObstaculo := velocidadObstaculo + 1;
   if velocidadObstaculo > 20 then
    velocidadObstaculo := 20;
   end;

end;
end.
