interface ImportMetaEnv {
  /** SHA del commit desplegado (lo pasa la CI). */
  readonly PUBLIC_COMMIT?: string;
  /** URL de la ejecución de GitHub Actions que compiló el sitio. */
  readonly PUBLIC_RUN_URL?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
