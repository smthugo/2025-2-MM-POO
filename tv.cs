class Televisao
{
    private const int CanalMinimo = 0;
    private const int CanalMaximo = 520;
    private const int VolumeMinimo = 0;
    private const int VolumeMaximo = 100;

    private int canalAtual;
    private int ultimoCanalAssistido;
    private int volumeAtual;
    private bool estaMudo;

    public Televisao()
    {
        canalAtual = ultimoCanalAssistido;
        volumeAtual = 50;
        estaMudo = false;
    }

    public void Ligar()
    {
        canalAtual = ultimoCanalAssistido;
        Console.WriteLine($"TV ligada no canal {canalAtual}");
    }

    public void AumentarCanal()
    {
        if (canalAtual < CanalMaximo)
        {
            canalAtual++;
            ultimoCanalAssistido = canalAtual;
        }
    }

    public void ReduzirCanal()
    {
        if (canalAtual > CanalMinimo)
        {
            canalAtual--;
            ultimoCanalAssistido = canalAtual;
        }
    }

    public void IrParaCanal(int numeroCanal)
    {
        if (numeroCanal >= CanalMinimo && numeroCanal <= CanalMaximo)
        {
            canalAtual = numeroCanal;
            ultimoCanalAssistido = canalAtual;
        }
        else
        {
            Console.WriteLine("Canal inválido.");
        }
    }

    public void AumentarVolume()
    {
        if (!estaMudo && volumeAtual < VolumeMaximo)
        {
            volumeAtual++;
        }
    }

    public void ReduzirVolume()
    {
        if (!estaMudo && volumeAtual > VolumeMinimo)
        {
            volumeAtual--;
        }
    }

    public void AtivarMudo()
    {
        estaMudo = true;
    }

    public void DesativarMudo()
    {
        estaMudo = false;
    }

    public void ExibirStatus()
    {
        string statusVolume = estaMudo ? "Mudo" : volumeAtual.ToString();
        Console.WriteLine($"Canal atual: {canalAtual} | Volume: {statusVolume}");
    }
}
